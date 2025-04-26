from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from utils import get_db, hash_password, verify_password, create_access_token, get_current_user
from models.user import User
from pydantic import BaseModel
from schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/register", response_model=UserResponse)
async def register(request: UserCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем, существует ли пользователь с таким email
    result = await db.execute(select(User).where(User.email == request.email))
    user = result.scalars().first()

    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Создаем нового пользователя
    new_user = User(
        name=request.name,
        email=request.email,
        password_hash=hash_password(request.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    # Проверяем, существует ли пользователь с таким email
    result = await db.execute(select(User).where(User.email == request.email))
    user = result.scalars().first()

    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Создаем JWT-токен
    access_token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user
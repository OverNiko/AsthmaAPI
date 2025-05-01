from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone
from models.symptom import Symptom
from schemas.symptom import SymptomCreate, SymptomResponse
from utils import get_db, get_current_user
from models.user import User

router = APIRouter(
    prefix="/symptoms",
    tags=["Symptoms"],
)

@router.post("/", response_model=SymptomResponse)
async def create_symptom(
    symptom: SymptomCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Создаем новую запись симптомов
    new_symptom = Symptom(
        cough_level=symptom.cough_level,
        breathlessness=symptom.breathlessness,
        user_id=current_user.id
    )
    db.add(new_symptom)
    await db.commit()
    await db.refresh(new_symptom)

    return new_symptom

@router.get("/", response_model=list[SymptomResponse])
async def read_symptoms(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Symptom).where(Symptom.user_id == current_user.id).options(joinedload(Symptom.user)))
    symptoms = result.scalars().all()

    return symptoms

@router.get("/history", response_model=list[SymptomResponse])
async def get_symptom_history(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Получаем все записи симптомов текущего пользователя
    result = await db.execute(
        select(Symptom)
        .where(Symptom.user_id == current_user.id)
        .order_by(Symptom.timestamp.desc())  # Сортировка по времени (новые записи первыми)
    )
    symptoms = result.scalars().all()

    return symptoms

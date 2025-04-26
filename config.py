from environs import Env
import os

env = Env()
env.read_env()

DATABASE_URL = os.getenv("DATABASE_URL", env.str("DATABASE_URL"))
SECRET_KEY = env.str("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


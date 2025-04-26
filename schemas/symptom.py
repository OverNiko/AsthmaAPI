from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class SymptomCreate(BaseModel):
    cough_level: int = Field(..., ge=0, le=10, description="Уровень кашля (0–10)")
    breathlessness: int = Field(..., ge=0, le=10, description="Уровень одышки (0–10)")

class SymptomResponse(BaseModel):
    id: int
    cough_level: int
    breathlessness: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

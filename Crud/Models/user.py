from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class user(BaseModel):
    username: str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo: str
    creacion_user: datetime = datetime.now()


class userId(BaseModel):
    id: int


class ShowUser(BaseModel):
    username: str
    nombre: str
    apellido:str
    correo: str

    class Config:
        orm_mode = True

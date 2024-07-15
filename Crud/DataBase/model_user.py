from datetime import datetime
from Crud.DataBase.db_Config import Base
from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "Usuarios"
    __table_args__ = {'extend_existing': True}  # Permitir redefinir la tabla si ya existe
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    nombres = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String, unique=True)
    creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    estado = Column(Boolean, default=False)
    ventas = relationship("Ventas", backref="usuario", cascade="all, delete-orphan")


class Ventas(Base):
    __tablename__ = "Ventas"
    __table_args__ = {'extend_existing': True}  # Permitir redefinir la tabla si ya existe
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id", ondelete="CASCADE"))
    venta = Column(Integer)
    ventas_productos = Column(Integer)

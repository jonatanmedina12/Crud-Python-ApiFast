from fastapi import APIRouter, Depends, HTTPException
from Crud.Models.user import userId, user, ShowUser
from Crud.DataBase.db_Config import get_db
from Crud.DataBase.model_user import User
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["usuario"]
)

@router.post('/crear_usuario')
def crear_usuario(user_petition: user, db: Session = Depends(get_db)):
    usuario = user_petition.dict()
    print(usuario)
    nuevo_usuario = User(
        username=usuario["username"],
        password=usuario["password"],
        nombres=usuario["nombres"],
        apellido=usuario["apellido"],
        direccion=usuario["direccion"],
        telefono=usuario["telefono"],
        correo=usuario["correo"],
        estado=usuario["estado"]
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"Respuesta": "Usuario creado satisfactoriamente", "usuario": nuevo_usuario}

@router.get('/get_user/{user_id}', response_model=ShowUser)
def traer_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no registrado")
    return usuario

@router.delete('/delete_user/{user_id}')
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == user_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"respuesta": "Usuario eliminado correctamente"}

@router.put('/update_user/{user_id}')
def actualizar_usuario(user_id: int, update_user: user, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == user_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.username = update_user.username
    usuario.password = update_user.password
    usuario.nombres = update_user.nombres
    usuario.apellido = update_user.apellido
    usuario.direccion = update_user.direccion
    usuario.telefono = update_user.telefono
    usuario.correo = update_user.correo
    usuario.estado = update_user.estado

    db.commit()
    db.refresh(usuario)
    return {"respuesta": "Usuario actualizado correctamente", "usuario": usuario}

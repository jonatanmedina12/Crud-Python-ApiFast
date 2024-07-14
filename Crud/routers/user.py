from fastapi import APIRouter
from Crud.Models.user import userId,user
router = APIRouter(

    prefix="/user",
    tags=["usuario"]

)

usuarios = []

@router.post('/crear_usuario')
def crear_usuario(user_petition: user):
    usuario = user_petition.dict()
    usuarios.append(usuario)

    print(usuario)

    return {"Respuesta": "Usuario creado satisfactoriamente"}


@router.get('/get_user')
def traer_usuario():
    return usuarios


@router.post('/get_user_id/{user_id}')
def obtener_usuario(user_id: int):
    for item_user in usuarios:
        if item_user["id"] == user_id:
            return {'usuario:': item_user["nombre"]}
    return {"respuesta": "usuario no encontrado"}


@router.post('/get_user_id_')
def obtener_usuario_json(user_id: userId):
    for item_user in usuarios:
        if item_user["id"] == user_id.id:
            return {'usuario:': item_user["apellido"]}
    return {"respuesta": "usuario no encontrado"}


@router.delete('/delete_user/{user_id}')
def eliminar_usuario(user_id: int):
    for index, user_ in enumerate(usuarios):
        print(index, user_)
        if user_["id"] == user_id:
            usuarios.pop(index)
            return {"respuesta": "Usuario eliminado correctamente"}
    return {"respuesta": "usuario no encontrado"}


@router.put('/update_user/{user_id}')
def actualizar_usuario(user_id: int, update_user: user):
    for index, user_ in enumerate(usuarios):
        if user_["id"] == user_id:
            usuarios[index]["id"] = update_user.dict()["id"]
            usuarios[index]["nombre"] = update_user.dict()["nombre"]
            usuarios[index]["apellido"] = update_user.dict()["apellido"]
            usuarios[index]["direccion"] = update_user.dict()["direccion"]
            usuarios[index]["telefono"] = update_user.dict()["telefono"]
            return {"respuesta": "Usuario actualizado correctamente"}
    return {"respuesta": "usuario no encontrado"}

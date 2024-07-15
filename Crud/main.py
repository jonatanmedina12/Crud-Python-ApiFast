from fastapi import FastAPI
import uvicorn
from DataBase.db_Config import Base, engine
from DataBase.model_user import User, Ventas  # Asegúrate de importar todos los modelos

from routers.Routers import router


def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print("Tablas creadas exitosamente")
    except Exception as e:
        print(f"Error creando las tablas: {e}")

try:
    create_tables()
except Exception as e:
    print(f"Error al ejecutar create_tables: {e}")

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

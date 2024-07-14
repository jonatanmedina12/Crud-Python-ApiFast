from fastapi import FastAPI
import uvicorn

from routers.user import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

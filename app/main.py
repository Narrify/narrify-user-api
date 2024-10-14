"Main file for the FastAPI application"
import uvicorn
from fastapi import FastAPI, status
from app.db.database import Base, engine
from app.router.users_router import router as user_router
from app.api.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Narrify | User Management API",
    description="User management API for Narrify.",
    version="1.0.0",
)

@app.get("/", status_code=status.HTTP_200_OK)
async def hello_world():
    """
    TODO
    """

    return "Hello World"

app.include_router(auth_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app)

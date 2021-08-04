from fastapi import FastAPI
import uvicorn
from backend.routers.menu import router as MenuRouter
from backend.routers.user import router as UserRouter
from backend.routers.plan import router as PlanRouter

app = FastAPI()

app.include_router(MenuRouter, tags=["Menu"], prefix="/menu")
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(PlanRouter, tags=["Plan"], prefix="/plan")

@app.get("/", tags=["Root"])
async def home():
    return {"message": "Welcome"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)
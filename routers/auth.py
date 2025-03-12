from fastapi import APIRouter

router = APIRouter()


@app.get("/auth/")
async def get_user():
    return {"user": "authenicated"}

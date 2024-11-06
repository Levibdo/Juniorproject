from fastapi import FastAPI
from pydantic import BaseModel
from config import VERSION
from routers.usuarios import router as usuarios_router


app = FastAPI(version=VERSION)
app.include_router(usuarios_router)


class Version(BaseModel):
    version: str


@app.get("/", response_model=Version)
async def health():
    return {"version": app.version}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

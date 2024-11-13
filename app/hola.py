from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://comoestas:8001/comoestas")
    return {"message": "Hola", "response_from_comoestas": response.json()}

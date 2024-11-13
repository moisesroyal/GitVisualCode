from fastapi import FastAPI

app = FastAPI()

@app.get("/comoestas")  
async def read_root():
    return {"message": "¿Cómo estás?"}

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def raiz():
    return JSONResponse(content={"message": "Oi Mozão, ta bem?"})

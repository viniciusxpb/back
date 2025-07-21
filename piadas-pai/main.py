from fastapi import FastAPI
from fastapi.responses import JSONResponse
import openai
import os

# Substitua pela sua chave da OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    openai.api_key = api_key
else:
    print("⚠️ Chave da OpenAI não encontrada. Endpoints de IA vão falhar.")

    
app = FastAPI(
    title="Joker API",
    description="API que responde piadas e trauma, igual sua ex.",
    version="1.0.0"
)

@app.get("/")
async def raiz():
    return JSONResponse(content={"message": "Oi Mozão, ta bem?"})

@app.get("/piada")
async def piada():
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Me conta uma piada boa e curta."}
            ],
            temperature=0.7,
            max_tokens=50
        )

        piada = resposta.choices[0].message.content.strip()
        return JSONResponse(content={"piada": piada})

    except Exception as e:
        return JSONResponse(content={"erro": str(e)}, status_code=500)

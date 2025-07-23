import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from openai import OpenAI

load_dotenv()  # carrega .env localmente

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("❌ Chave da OpenAI não encontrada. O palhaço morreu antes de contar a piada. Verifica o .env ou configura no Render, campeão.")

client = OpenAI(api_key=api_key)

app = FastAPI(
    title="Joker API",
    description="API que responde piadas e trauma, igual sua ex.",
    version="1.0.0"
)

@app.get("/")
async def raiz():
    return JSONResponse(content={"message": "Morgana Rules"})

@app.get("/piada")
async def piada(topico: str = "aleatório"):
    try:
        prompt = f"Me conta uma piada boa, curta e criativa sobre o tema: {topico}."

        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=50
        )

        piada = resposta.choices[0].message.content.strip()
        return JSONResponse(content={"piada": piada})

    except Exception as e:
        return JSONResponse(content={"erro": f"💀 Erro ao gerar piada: {str(e)}"}, status_code=500)

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from openai import OpenAI

client = OpenAI(
    api_key=""
)

app = FastAPI(
    title="Joker API",
    description="API que responde piadas e trauma, igual sua ex.",
    version="1.0.0"
)

@app.get("/")
async def raiz():
    return JSONResponse(content={"message": "Morgana Rules"})

@app.get("/piada")
async def piada(topico: str = Query("aleatório", description="Tópico da piada")):
    try:
        prompt = f"Me conta uma piada boa, curta e criativa sobre o tema: {topico}."

        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=50
        )

        piada = resposta.choices[0].message.content.strip()
        return JSONResponse(content={"topico": topico, "piada": piada})

    except Exception as e:
        return JSONResponse(content={"erro": str(e)}, status_code=500)

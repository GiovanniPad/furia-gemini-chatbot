import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from google.genai import Client

if os.getenv("RENDER") is None:
    from dotenv import load_dotenv
    load_dotenv()

app = FastAPI()
client = Client(api_key=os.getenv("GEMINI_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "https://furia-gemini-chatbot.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota da API para conversar com o Gemini
@app.get("/chat")
async def chat(query: str):
    question = query.strip()
    scope = (
        "Você deve responder perguntas apenas sobre o time de CS da "
        "organização de e-sports Fúria, caso a pessoa insira uma pergunta que não seja sobre "
        "ela, você não deve responder. Levando isso em consideração, responda a "
        f"seguinte pergunta: {question}"
    )
    response = client.models.generate_content(model="gemini-2.0-flash", contents=scope)
    return {"response": response.text}


# Serve a pasta "frontend" como arquivos estáticos
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

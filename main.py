from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from deep_translator import GoogleTranslator

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/translate")
def translate_text(text: str = Query(...), lang: str = Query(...)):
    try:
        translated = GoogleTranslator(source="auto", target=lang).translate(text)
        return {"translated_text": translated}
    except Exception as e:
        return {"error": str(e)}

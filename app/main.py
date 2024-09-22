from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.documents.router import router as router_documents

from app.document_text.router import router as router_documents_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def home_page():
    return {"message": "It Works!!!"}


app.include_router(router_documents)
app.include_router(router_documents_text)

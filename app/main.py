from fastapi import FastAPI

from documents.router import router as router_documents

from document_text.router import router as router_documents_text

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "It Works!!!"}


app.include_router(router_documents)
app.include_router(router_documents_text)

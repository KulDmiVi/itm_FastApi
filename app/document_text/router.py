from fastapi import APIRouter
from celery_worker.celeryapp import img_to_text
from app.documents.dao import DocumentsDAO



router = APIRouter(tags=['Документы'])


@router.post("/doc_analyse/{document_id}", summary="Добавить описание")
async def doc_analyse(document_id: int) -> dict:
    document = await DocumentsDAO.get_document_by_id(document_id)
    img_to_text.delay(document.path, document_id)
    return {"status": "200 ok"}

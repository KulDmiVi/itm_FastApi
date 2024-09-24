from fastapi import APIRouter, Response
from app.celery_worker.app import img_to_text
from app.document_text.dao import DocumentsTextDAO


router = APIRouter(tags=['Документы'])


@router.post("/doc_analyse/{document_id}", summary="Добавить описание")
def doc_analyse(document_id: int) -> dict:
    img_to_text.delay(document_id)
    return {"status": "200 ok"}


@router.get("/get_text/{document_id}", summary="Удаление документа по id", status_code=200)
async def get_document(response: Response, document_id: int) -> dict:
    text_document = await DocumentsTextDAO.get_document_text(document_id)
    if text_document:
        return text_document.as_dict()
    else:
        response.status_code = 204
        return {'message': 'No Content'}

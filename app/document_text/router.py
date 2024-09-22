from fastapi import APIRouter
from app.document_text.analyzer import img_to_text
from app.document_text.dao import DocumentsTextDAO
from app.documents.dao import DocumentsDAO
from app.document_text.models import DocumentsText


router = APIRouter(tags=['Документы'])


@router.post("/doc_analyse/{document_id}", summary="Добавить описание")
async def doc_analyse(document_id: int) -> dict:
    document = await DocumentsDAO.get_document_by_id(document_id)
    text = img_to_text(document.path)
    new_doc_text = DocumentsText()
    new_doc_text.id_doc = document_id
    new_doc_text.text = text
    text_id = await DocumentsTextDAO.add_document_text(new_doc_text)
    return {"text": text, 'id': text_id}

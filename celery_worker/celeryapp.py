from celery import Celery
import pytesseract
from PIL import Image
from app.document_text.models import DocumentsText
from app.document_text.dao import DocumentsTextDAO

CELERY_BROKER_URL = 'pyamqp://rmuser:rmpassword@127.0.0.1:5672//'
celerymq = Celery("text_analyzer", broker=CELERY_BROKER_URL)


@celerymq.task
async def img_to_text(img_path: str, document_id: int):
    print('123')
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # text = pytesseract.image_to_string(Image.open(img_path), lang='rus')
    # new_doc_text = DocumentsText()
    # new_doc_text.id_doc = document_id
    # new_doc_text.text = text
    # id = await DocumentsTextDAO.add_document_text(new_doc_text)
    # return id
    #



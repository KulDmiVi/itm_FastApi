import pytesseract
from PIL import Image
from celery import Celery
from celery.utils.log import get_task_logger

from app.document_text.dao import DocumentsTextDAO
from app.document_text.models import DocumentsText

CELERY_BROKER_URL = 'amqp://rmuser:rmpassword@rabbitmq:5672'
celerymq = Celery("text_analyzer", broker=CELERY_BROKER_URL)
celery_log = get_task_logger(__name__)


@celerymq.task
def img_to_text(img_path: str, document_id: int):
    celery_log.info(f"Order Complete!")
    text = pytesseract.image_to_string(Image.open(img_path), lang='rus')
    new_doc_text = DocumentsText()
    new_doc_text.id_doc = document_id
    new_doc_text.text = text
    id = DocumentsTextDAO.add_document_text(new_doc_text)
    return id

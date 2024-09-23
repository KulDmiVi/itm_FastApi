import pytesseract
from PIL import Image
from celery import Celery
from celery.utils.log import get_task_logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.document_text.models import DocumentsText

DATABASE_URL = "postgresql+asyncpg://test_user:test_pas@db/test_db"
CELERY_BROKER_URL = 'amqp://rmuser:rmpassword@rabbitmq:5672'

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)

celerymq = Celery("text_analyzer", broker=CELERY_BROKER_URL)
celery_log = get_task_logger(__name__)


@celerymq.task
async def img_to_text(img_path: str, document_id: int):
    celery_log.info(f"Order Complete!")
    text = pytesseract.image_to_string(Image.open(img_path), lang='rus')
    new_doc_text = DocumentsText()
    new_doc_text.id_doc = document_id
    new_doc_text.text = text
    with session_maker() as session:
        with session.begin():
            session.add(new_doc_text)
            session.commit()
    celery_log.info(f"Order Complete!!!!!")
    return text

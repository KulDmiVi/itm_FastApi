import pytesseract
from PIL import Image
from celery import Celery


from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from app.document_text.models import DocumentsText
from app.documents.models import Documents

DATABASE_URL = "postgresql+psycopg2://test_user:test_pas@db/test_db"
CELERY_BROKER_URL = 'amqp://rmuser:rmpassword@rabbitmq:5672'

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)

celerymq = Celery("text_analyzer", broker=CELERY_BROKER_URL)


@celerymq.task
def img_to_text(document_id: int):
    with session_maker() as session:
        with session.begin():
            query = select(Documents).filter_by(id=document_id)
            result = session.execute(query)
            document = result.scalar_one_or_none()
            text = pytesseract.image_to_string(Image.open(document.path), lang='rus')
            new_doc_text = DocumentsText()
            new_doc_text.id_doc = document_id
            new_doc_text.text = text
            session.add(new_doc_text)
            session.flush()
            session.commit()
    return text

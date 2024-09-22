import os

from sqlalchemy import select, delete

from app.database import async_session_maker, Base
from app.document_text.models import DocumentsText


class DocumentsTextDAO:
    model = DocumentsText
    @classmethod
    async def add_document_text(cls, new_document_text: DocumentsText):
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_document_text)
                await session.flush()
                new_document_text_id = new_document_text.id
                await session.commit()
                return new_document_text_id

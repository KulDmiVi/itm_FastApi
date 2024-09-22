import os

from sqlalchemy import select, delete

from app.database import async_session_maker, Base
from app.documents.models import Documents


class DocumentsDAO:
    model = Documents

    @classmethod
    async def add_document(cls, new_document: Documents):
        async with async_session_maker() as session:
            async with session.begin():
                session.add(new_document)
                await session.flush()
                new_document_id = new_document.id
                await session.commit()
                return new_document_id

    @classmethod
    async def delete_document_by_id(cls, document_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=document_id)
                result = await session.execute(query)
                document_to_delete = result.scalar_one_or_none()
                if not document_to_delete:
                    return None
                file_to_delete = document_to_delete.path
                if os.path.isfile(file_to_delete):
                    os.remove(file_to_delete)

                await session.execute(
                    delete(cls.model).filter_by(id=document_id)
                )
                await session.commit()
                return document_id

    @classmethod
    async def get_document_by_id(cls, document_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=document_id)
                result = await session.execute(query)
                document = result.scalar_one_or_none()
                if not document:
                    return None
                return document

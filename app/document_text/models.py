from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class DocumentsText(Base):
    """Модель описание загруженных документов"""

    __tablename__ = 'documentstext'
    id = Column(Integer(), primary_key=True)
    text = Column(Text(), nullable=False)
    id_doc = Column(Integer(), ForeignKey('documents.id'))
    document = relationship("Documents", backref="documents")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"text={self.text!r},"
                f"id_doc={self.id_doc!r})")

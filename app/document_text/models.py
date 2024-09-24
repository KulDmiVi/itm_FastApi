from sqlalchemy import Column, Integer, Text, ForeignKey
from app.database import Base


class DocumentsText(Base):
    """Модель описание загруженных документов"""
    __tablename__ = 'documentstext'
    id = Column(Integer(), primary_key=True)
    text = Column(Text(), nullable=False)
    id_doc = Column(Integer(), ForeignKey('documents.id',  ondelete="CASCADE"))


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"text={self.text!r},"
                f"id_doc={self.id_doc!r})")

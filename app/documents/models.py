from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


from app.database import Base

class Documents(Base):
    """Модель загруженные документы"""

    __tablename__ = 'documents'
    id = Column(Integer(), primary_key=True)
    path = Column(String(255), nullable=False)
    date = Column(DateTime, default=func.now())
    docText = relationship("DocumentsText", backref="documentstext")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"path={self.path!r},"
                f"date={self.date!r})")

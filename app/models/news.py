from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
    Integer)
from app.core.database import Base, engine


class News(Base):
    """Model Auth Users
    """

    __tablename__ = "news"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(25))
    title = Column(String(100))
    link = Column(String(242))
    status = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)

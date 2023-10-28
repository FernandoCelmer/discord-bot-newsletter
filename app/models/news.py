from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Date,
    String,
    Integer
)
from app.core.database import Base, engine


class News(Base):
    """Model News
    """

    __tablename__ = "news"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(75))
    category = Column(String(25))
    url = Column(String(145))
    thumbnail = Column(String(145))
    description = Column(String(100))
    status = Column(Boolean, default=False)
    scheduled = Column(Date)
    created_date = Column(
        DateTime,
        default=datetime.utcnow
    )
    update_date = Column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)

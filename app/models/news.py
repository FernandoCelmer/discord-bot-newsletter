import uuid

from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Date,
    String,
    Integer,
    Uuid
)
from app.core.database import Base, engine


class News(Base):
    """Model News
    """

    __tablename__ = "news"
    __table_args__ = {'extend_existing': True}

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(75))
    category = Column(String(25))
    url = Column(String(145))
    thumbnail = Column(String(145))
    description = Column(String(100))
    status = Column(Boolean, default=False)
    scheduled = Column(Date, index=True)
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

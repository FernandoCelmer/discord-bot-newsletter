from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
    Integer
)
from app.core.database import Base, engine


class Channel(Base):
    """Model Channel
    """

    __tablename__ = "channel"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    status = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)

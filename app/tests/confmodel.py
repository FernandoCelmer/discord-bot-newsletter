from datetime import datetime
from sqlalchemy import Boolean, Column, Integer
from app.core.database import Base


class Item(Base):

    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=True)

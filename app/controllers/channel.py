from sqlalchemy.orm import Session

from app.core.controller import BaseController
from app.models.channel import Channel


class ControllerChannel(BaseController):

    def __init__(self, db: Session = None):
        super().__init__(db)
        self.model_class = Channel

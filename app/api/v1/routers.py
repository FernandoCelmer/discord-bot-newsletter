from fastapi import APIRouter
from app.api.v1.endpoints import channel, news

router = APIRouter()
router.include_router(channel.router, tags=["Channel"])
router.include_router(news.router, tags=["News"])

from fastapi import FastAPI
from mangum import Mangum

from app import __version__
from app.api.v1.routers import router


app = FastAPI(
    title="Newsletter API",
    description="Newsletter Project API",
    version=__version__
)


app.include_router(router, prefix="/v1")
handler = Mangum(app)

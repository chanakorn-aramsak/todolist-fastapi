from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from api import tasks

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        # This sets the allowed HTTP methods for CORS requests
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        # This sets the allowed headers in CORS requests
        allow_headers=["Content-Type"],
    )

    '''
    For example, to only allow GET and POST methods and "Content-Type" header, update the middleware definition as follows:
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        # Only allowing GET and POST methods
        allow_methods=["GET", "POST"],
        # Only allowing the "Content-Type" header
        allow_headers=["Content-Type"],
    )

    '''
    _app.include_router(tasks.router)
    return _app


app = get_application()

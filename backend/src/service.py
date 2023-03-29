from fastapi.applications import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from src.api.endpoints.routers import api_router
from src.config.settings import BackendSettings, backend_settings


class BackendService:
    __slots__ = ("_settings", "_asgi_app")

    def __init__(self, settings: BackendSettings) -> None:
        """
        Initiation ASGI app.
        """
        self._settings = settings

        middleware = [
            Middleware(
                CORSMiddleware,
                allow_origins=self._settings.ALLOWED_ORIGINS,
                allow_credentials=True,
                allow_methods=self._settings.ALLOWED_METHODS,
                allow_headers=self._settings.ALLOWED_HEADERS,
            ),
        ]

        self._asgi_app = FastAPI(middleware=middleware, version=self._settings.VERSION)
        self._asgi_app.include_router(api_router)

    def get_app(self) -> FastAPI:
        """
        Get ASGI app.
        """
        return self._asgi_app

    def serve(self, path_to_app: str) -> None:
        """
        Start service.
        """
        autoreload = use_colors = False
        if self._settings.DEBUG:
            autoreload = use_colors = True

        run(
            path_to_app,
            host=self._settings.SERVER_HOST,
            port=self._settings.SERVER_PORT,
            workers=self._settings.SERVER_WORKERS,
            reload=autoreload,
            use_colors=use_colors,
        )


backend_service = BackendService(settings=backend_settings)

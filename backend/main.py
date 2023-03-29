from src.service import backend_service

app = backend_service.get_app()

if __name__ == "__main__":
    backend_service.serve("main:app")

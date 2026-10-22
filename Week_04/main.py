from fastapi import FastAPI

from api_service.Router.routes import router


app = FastAPI(
    title="Week 04 AI Service",
    description=(
        "AI service demonstrating "
        "interfaces and dependency injection"
    ),
    version="1.0.0",
)


app.include_router(
    router
)
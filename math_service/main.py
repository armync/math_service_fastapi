from fastapi import FastAPI

# dirs
from math_service.api.routes import router as math_router
from math_service.core.middleware import log_requests_middleware

# db
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="Microservice Mathematical Operations")  # instantiate

app.middleware("http")(
    log_requests_middleware
)  # attach middleware function to log each request

app.include_router(
    math_router, prefix="/calculate", tags=["Math Operations"]
)  # mount route handler from routes.py

# Register Tortoise
register_tortoise(
    app,
    db_url="sqlite://math_requests.db",
    modules={"models": ["math_service.models.request_log"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

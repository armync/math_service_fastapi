import time
from fastapi import Request
from math_service.services.logger import logger


# current HTTP request (method, path, headers etc)
# call_next lets FastAPI handle the request normally
async def log_requests_middleware(request: Request, call_next):
    start_time = time.time()

    # calls the next handler, the actual route function
    # e.g. it might go to /calculate/fib and run the Fibonacci logic.
    response = await call_next(request)

    # subtract start from end to get time spent (in seconds)
    duration = time.time() - start_time
    duration_ms = round(duration * 1000, 2)  # milliseconds

    logger.info(
        f"{request.method} {request.url.path} - {response.status_code} - {duration_ms}ms"
    )

    return response


# Sees who enters (request)
# Watches what happens (time spent)
# Logs details after they leave (response)

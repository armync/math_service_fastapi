from fastapi import APIRouter, Depends, HTTPException
from math_service.schemas.operations import (
    PowInput,
    FibInput,
    FactInput,
    OperationalResult,
)
from math_service.services.math_ops import calculate_pow, fibonacci, factorial
from math_service.services.logger import logger
from math_service.services.db_logger import log_request_to_db
from math_service.auth.api_key import verify_api_key
import time

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.post("/pow", response_model=OperationalResult)
async def pow_handler(payload: PowInput):
    logger.info(f"Received pow request: {payload.model_dump()}")

    try:
        start_time = time.time()
        result = calculate_pow(payload.base, payload.exponent)
        duration = round((time.time() - start_time) * 1000, 2)

        await log_request_to_db(
            operation="pow",
            input_data=payload.model_dump(),
            result=str(result),
            duration_ms=duration,
        )

        logger.info(
            f"pow({payload.base}, {payload.exponent}) = {result} [{duration:.2f}s]"
        )
        return {"result": result}

    except Exception:
        logger.error("Unhandled error in /pow", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/fib", response_model=OperationalResult)
async def fib_handler(payload: FibInput):
    logger.info(f"Received fib request: {payload.model_dump()}")

    try:
        start_time = time.time()
        result = fibonacci(payload.n)
        duration = round((time.time() - start_time) * 1000, 2)

        await log_request_to_db(
            operation="fib",
            input_data=payload.model_dump(),
            result=str(result),
            duration_ms=duration,
        )

        logger.info(f"fibonacci({payload.n}) = {result} [{duration:.2f}s]")
        return {"result": result}

    except Exception:
        logger.error("Unhandled error in /fib", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/fact", response_model=OperationalResult)
async def fact_handler(payload: FactInput):
    logger.info(f"Received factorial request: {payload.model_dump()}")

    try:
        start_time = time.time()
        result = factorial(payload.n)
        duration = round((time.time() - start_time) * 1000, 2)

        await log_request_to_db(
            operation="fact",
            input_data=payload.model_dump(),
            result=str(result),
            duration_ms=duration,
        )

        logger.info(f"factorial({payload.n}) = {result} [{duration:.2f}s]")
        return {"result": result}

    except Exception:
        logger.error("Unhandled error in /fact", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

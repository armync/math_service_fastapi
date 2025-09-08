from math_service.models.request_log import RequestLog


async def log_request_to_db(operation, input_data, result, duration_ms):
    await RequestLog.create(
        operation=operation,
        input_data=input_data,
        result=result,
        duration_ms=duration_ms,
    )

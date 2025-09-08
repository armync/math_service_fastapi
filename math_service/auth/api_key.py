from fastapi import Header, HTTPException, status
from math_service.core.config import API_KEY


def verify_api_key(x_api_key: str = Header(...)):
    # look for a header named x-api-key
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )

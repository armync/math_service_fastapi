from pydantic import BaseModel, Field  # inherit from BaseModel


class PowInput(BaseModel):  # pow(x,y)
    base: float = Field(..., example=2)  # (...) field required
    exponent: float = Field(..., example=3)


class FibInput(BaseModel):  # fibonacci(n); n = pos, ge = 0 (no negative)
    n: int = Field(..., ge=0, example=10)


class FactInput(BaseModel):  # factorial(n)
    n: int = Field(..., ge=0, example=5)


class OperationalResult(BaseModel):
    result: int | float  # serialize automatically in the response FastAPI

from functools import lru_cache  # built-in decorator that enables in-memory caching


def calculate_pow(base: float, exponent: float) -> float:
    return base**exponent  # fast and deterministic


@lru_cache(
    maxsize=128
)  # previous results are stored in memory - speedup. last 128 unique calls.
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=128)
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

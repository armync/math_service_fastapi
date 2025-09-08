# lightweight, dictionary-based cache


class SimpleCache:
    def __init__(self):
        self._store = {}  # cache — just a dictionary (like a mini database in memory)
        # stores key-value pairs, like: "fib_10" - 55

    def get(self, key):  # tries to fetch a cached value using the key
        return self._store.get(key)

    def set(self, key, value):  # adds or updates a cached value
        self._store[key] = value

    def clear(self):  # deletes all cached values
        self._store.clear()


# Example usage:
# cache = SimpleCache()
# cache.set("fib_10", 55)
# result = cache.get("fib_10")

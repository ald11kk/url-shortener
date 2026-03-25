import string
import random

url_storage = {}

def generate_short_code(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_short_url(long_url: str) -> str:
    short_code = generate_short_code()
    while short_code in url_storage:
        short_code = generate_short_code()
    url_storage[short_code] = long_url
    return short_code

def get_original_url(code: str) -> str | None:
    return url_storage.get(code)
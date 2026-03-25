import string
import random

url_storage = {}

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_short_url(long_url):
    short_code = generate_short_code()
    url_storage[short_code] = long_url
    return short_code

def get_long_url(short_code):
    return url_storage.get(short_code)
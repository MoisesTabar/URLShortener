import base64
import hashlib

def shorten_url(long_url: str) -> str:
    sha256 = hashlib.sha256(long_url.encode()).digest()

    base64_str = base64.urlsafe_b64encode(sha256).decode()
    
    base62_str = base64_to_base62(base64_str)

    return base62_str

def base64_to_base62(base64_str):
    base62_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    base64_int = int.from_bytes(base64_str.encode(), 'big')

    base62_str = ''
    while base64_int:
        base64_int, remainder = divmod(base64_int, 62)
        base62_str = base62_chars[remainder] + base62_str

    return base62_str
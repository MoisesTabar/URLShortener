import base64
import hashlib

def shorten_url(long_url: str) -> str:
    # Compute a SHA-256 hash of the URL
    sha256 = hashlib.sha256(long_url.encode()).digest()

    # Convert the hash to a base 64 string
    base64_str = base64.urlsafe_b64encode(sha256).decode()

    # Convert the base 64 string to a base 62 string
    base62_str = base64_to_base62(base64_str)

    return base62_str

def base64_to_base62(base64_str):
    # Define the characters to use for base 62 encoding
    base62_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Convert the base 64 string to an integer
    base64_int = int.from_bytes(base64_str.encode(), 'big')

    # Convert the integer to a base 62 string
    base62_str = ''
    while base64_int:
        base64_int, remainder = divmod(base64_int, 62)
        base62_str = base62_chars[remainder] + base62_str

    return base62_str
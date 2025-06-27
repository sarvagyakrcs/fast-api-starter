import random
import string

def generate_6_digit_code():
    return ''.join(random.choices(string.digits, k=6))
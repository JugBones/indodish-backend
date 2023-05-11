import logging
import random
import string

logger = logging.getLogger(__name__)
ALPHA_NUM = string.ascii_letters + string.digits


def generate_random_alphanumeric(length: int = 32) -> str:
    return "".join(random.choices(ALPHA_NUM, k=length))

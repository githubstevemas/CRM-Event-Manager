import os

from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key
)
from dotenv import load_dotenv

load_dotenv()


def get_public_key():

    public_key_pem = os.getenv("PUBLIC_KEY").replace("\\n",
                                                     "\n").encode()
    public_key = load_pem_public_key(public_key_pem)

    return public_key


def get_private_key():

    private_key_pem = os.getenv("PRIVATE_KEY").replace("\\n",
                                                       "\n").encode()
    private_key = load_pem_private_key(private_key_pem, password=None)

    return private_key

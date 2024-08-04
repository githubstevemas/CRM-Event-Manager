import secrets

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


secret_key = secrets.token_urlsafe(50)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()


private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')

with open('.env', 'a') as env_file:

    env_file.write("DB_PASSWORD=\n")
    env_file.write("DB_USERNAME=\n")
    env_file.write(f"SECRET_KEY={secret_key}")
    env_file.write(f"\nPRIVATE_KEY=\"{private_pem.replace('\n',
                                                          '\\n')}\"\n")
    env_file.write(f"PUBLIC_KEY=\"{public_pem.replace('\n',
                                                      '\\n')}\"\n")

import os
import secrets
import sys

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from config.config import Base, main_engine


def generate_dotenv():
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


def create_tables_in_db():
    try:
        Base.metadata.create_all(main_engine)
    except Exception as e:
        print(f"Error while creating : {e}")


def generate_menu():
    while True:
        print("\n[1] Generate .env file")
        print("[2] Create tables in db")
        print("[0] Exit\n")
        choice = input("Your choice ? ")

        if choice == "1":
            generate_dotenv()
            sys.exit()

        elif choice == "2":

            if os.path.exists('.env'):
                print("\nMake sure you have set your ids.")
                input("Press Enter to continue.")
                create_tables_in_db()
                sys.exit()
            else:
                print("\nYou must generate .env first.")

        elif choice == "0":
            sys.exit()


if __name__ == "__main__":
    generate_menu()

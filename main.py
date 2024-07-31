import argparse
import getpass

from epic_events.controllers.authentication import is_email_exists, \
    create_encrypted_token


def main():

    parser = argparse.ArgumentParser(description="Access to main app")
    parser.add_argument('email', type=str, help="User's email")
    args = parser.parse_args()

    exists = is_email_exists(args.email)

    if exists:
        print(f"Please enter your password : ")
        password = getpass.getpass("")

        create_encrypted_token(args.email)

    else:
        print("Wrong email.")


if __name__ == "__main__":
    main()

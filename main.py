import argparse
import getpass

from epic_events.controllers.auth_controller import is_email_exists
from epic_events.controllers.user_controller import main_menu


def main():

    parser = argparse.ArgumentParser(description="Access to main app")

    parser.add_argument('email', type=str, help="User's email")

    args = parser.parse_args()

    exists = is_email_exists(args.email)

    if exists:
        print(f"Welcome back {args.email} !\nPlease enter your password : ")
        password = getpass.getpass("")
    else:
        print("Wrong email.")

    main_menu()


if __name__ == "__main__":
    main()

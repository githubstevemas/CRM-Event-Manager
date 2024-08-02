import argparse

from epic_events.controllers.user_controller import main_menu
from epic_events.controllers.authentication import main_login


def main():

    parser = argparse.ArgumentParser(description="Access to main app")
    parser.add_argument('email', type=str, help="User's email")
    args = parser.parse_args()

    main_login(args)

    main_menu()


if __name__ == "__main__":
    main()

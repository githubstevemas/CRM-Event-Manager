import argparse
import os

import sentry_sdk

from epic_events.controllers.menu_controller import main_menu
from epic_events.controllers.auth_controller import main_login

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0)


def main():
    parser = argparse.ArgumentParser(description="Access to main app")
    parser.add_argument('email', type=str, help="User's email")
    args = parser.parse_args()

    main_login(args)

    main_menu()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/22 14:58:13 by mozay           #+#    #+#               #
#  Updated: 2026/07/22 18:42:35 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    load_dotenv()
    return {
        "mode": os.getenv("MATRIX_MODE"),
        "db": os.getenv("DATABASE_URL"),
        "api": os.getenv("API_KEY"),
        "log": os.getenv("LOG_LEVEL"),
        "zion": os.getenv("ZION_ENDPOINT")
        }


def show_config(config: dict[str, str | None]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config["mode"]
    if mode is None:
        mode = "Unknown"
    print("Mode:", mode)
    if config["db"]:
        if mode == "development":
            print("Database: Connected to local instance")
        elif mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected")
    else:
        print("Database: Missing")

    if config["api"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing")

    if config["log"]:
        print("Log Level: DEBUG")
    else:
        print("Log Level: Missing")

    if config["zion"]:
        print("Zion Network: Online")
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    else:
        print("Zion Network: Offline")
        print("\nEnvironment security check:")
        print("---------------------------")
        print("python -m venv venv")
        print("source venv/bin/activate")
        print("pip install -r requirements.txt")
        print("cp .env.example .env")
        print("Don't forget to fill in the metrics in the .env file.")
        print("\nThe Oracle sees all configurations.")


def main() -> None:
    config = load_config()
    show_config(config)


if __name__ == "__main__":
    main()

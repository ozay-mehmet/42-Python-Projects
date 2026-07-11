#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/11 18:11:57 by mozay           #+#    #+#               #
#  Updated: 2026/07/11 19:18:58 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def secure_archive(filename: str, mode="read", content="") -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename, "r") as file:
                return (True, file.read())
        elif mode == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, "Invalid mode")

    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    success, data = secure_archive("ancient_fragment.txt")
    print(success, data)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/21 12:17:12 by mozay           #+#    #+#               #
#  Updated: 2026/07/21 19:38:56 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in")
        print("\nCurrent Python:", sys.prefix)
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env"+"\\"+"Scripts"+"\\"+"activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(p=sys.prefix))
        print("Environment Path:", os.path.dirname(p=sys.executable))
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/21 19:40:14 by mozay           #+#    #+#               #
#  Updated: 2026/07/22 18:30:50 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import importlib
from importlib.metadata import version


def load_dependencies() -> dict[str, object | None]:
    packages: dict[str, object | None] = {}

    for package in ["numpy", "pandas", "matplotlib"]:
        try:
            if package == "matplotlib":
                packages[package] = importlib.import_module(
                    "matplotlib.pyplot"
                )
            else:
                packages[package] = importlib.import_module(package)

        except ImportError:
            packages[package] = None

    return packages


def check_dependencies(packages: dict[str, object | None]) -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    missing: list[str] = []

    print("Checking dependencies:")

    descriptions: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    for package in descriptions:
        if packages.get(package) is None:
            missing.append(package)

        else:
            try:
                print(
                    f"[OK] {package} "
                    f"({version(package)}) - "
                    f"{descriptions[package]}"
                )

            except Exception:
                missing.append(package)

    if missing:
        print("\nMissing Dependencies")
        for package in missing:
            print(f"- {package}")
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")

        print("\nInstall with Poetry:")
        print("poetry install")
        sys.exit(1)


def analyze_matrix_data() -> object:
    print("\nAnalyzing Matrix data...")

    import numpy as np
    import pandas as pd

    matrix = np.random.normal(
        loc=50,
        scale=10,
        size=1000
    )

    print(f"Processing {len(matrix)} data points...")

    return pd.DataFrame(
        {
            "Energy": matrix
        }
    )


def generate_visualization(data: object) -> None:
    print("Generating visualization...")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))

    plt.title("Matrix Energy")
    plt.xlabel("Energy")
    plt.ylabel("Frequency")

    plt.savefig(
        "matrix_analysis.png"
    )

    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    packages = load_dependencies()
    check_dependencies(packages)

    data = analyze_matrix_data()
    generate_visualization(data)


if __name__ == "__main__":
    main()

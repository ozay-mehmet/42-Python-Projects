#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mozay <mozay@student.42kocaeli.com.tr>    +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/21 19:40:14 by mozay           #+#    #+#               #
#  Updated: 2026/07/22 14:56:12 by mozay           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import importlib
from importlib.metadata import version


def load_dependencies() -> dict[str, object | None]:
    modules: dict[str, object | None] = {}
    for name in ["pandas", "numpy", "matplotlib"]:
        try:
            if name == "matplotlib":
                modules[name] = importlib.import_module("matplotlib.pyplot")
            else:
                modules[name] = importlib.import_module(name)
        except ImportError:
            modules[name] = None
    return modules


def check_dependencies(modules: dict[str, object | None]) -> None:
    missing: list[str] = []
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    packages = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready")
    ]

    for pkg, desc in packages:
        if modules.get(pkg) is None:
            missing.append(pkg)
        else:
            try:
                pkg_version = version(pkg)
                print(f"[OK] {pkg} ({pkg_version}) - {desc}")
            except Exception:
                missing.append(pkg)

    if missing:
        print("\nMissing Dependencies")
        for package in missing:
            print(f"- {package}")
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("poetry install")
        sys.exit(1)


def analyze_matrix_data(np: numpy, pd: pandas) -> object:
    print("\nAnalyzing Matrix data...")
    matrix_data = np.random.normal(loc=50, scale=10, size=1000)
    print(f"Processing {len(matrix_data)} data points...")
    df = pd.DataFrame({"Energy": matrix_data})
    return df


def generate_visualization(df: pandas.DataFrame,
                           plt: matplotlib.pyplot) -> None:
    print("Generating visualization...\n")
    plt.figure(figsize=(8, 5))
    plt.hist(df["Energy"], bins=30)
    plt.title("Matrix Energy")
    plt.xlabel("Energy")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    modules = load_dependencies()
    check_dependencies(modules)

    df = analyze_matrix_data(modules["numpy"], modules["pandas"])
    generate_visualization(df, modules["matplotlib"])


if __name__ == "__main__":
    main()

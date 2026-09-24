import sys
import importlib


def check() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    package_info = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
    }
    missing = False
    for p in package_info:
        try:
            lib = importlib.import_module(p)
            ver = getattr(lib, '__version__', 'unknown')
            print(f"[OK] {p} ({ver}) - {package_info[p]} ready")
        except ImportError:
            print(f"[MISSING] {p}")
            missing = True
    if missing:
        print("\nMissing dependencies detected.")
        print("To install using pip:")
        print("$> pip install -r requirements.txt")
        print("\nTo install using Poetry:")
        print("$> poetry install")
        print("$> poetry run python loading.py")
        sys.exit(1)


def show_versions() -> None:
    print("\n--- Installed Package Versions ---")
    package_list = ["pandas", "numpy", "matplotlib"]
    for p in package_list:
        try:
            lib = importlib.import_module(p)
            ver = getattr(lib, '__version__', 'unknown')
            print(f"{p:<12}: {ver}")
        except ImportError:
            pass
    print("\n--- pip vs Poetry Differences ---")
    print("pip    : Uses requirements.txt. Standard package installer,")
    print("         lacks strict dependency lockfiles by default.")
    print("Poetry : Uses pyproject.toml and poetry.lock. Provides")
    print("         strict dependency resolution and venv management.")


def run_simulation() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    raw_wave = np.random.randn(1000).cumsum()
    matrix_df = pd.DataFrame({"wave": raw_wave})
    matrix_df["smooth_trend"] = matrix_df["wave"].rolling(window=50).mean()
    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        matrix_df.index,
        matrix_df["wave"],
        label="Matrix Signal",
        color="green",
        alpha=0.5
    )
    ax.plot(
        matrix_df.index,
        matrix_df["smooth_trend"],
        label="Trend",
        color="lime",
        linewidth=2
    )
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Time")
    ax.set_ylabel("Signal Strength")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)
    fig.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check()
    show_versions()
    run_simulation()

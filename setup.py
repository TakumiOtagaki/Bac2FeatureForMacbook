from pathlib import Path
import runpy


def main():
    setup_path = Path(__file__).parent / "bac2feature" / "setup.py"
    runpy.run_path(setup_path)


if __name__ == "__main__":
    main()

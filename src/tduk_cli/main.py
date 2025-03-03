# tduk_cli/main.py (if using argparse)
import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple hello CLI.")
    parser.add_argument("--name", nargs="?", default="World", help="The name to greet.")
    args = parser.parse_args()

    print(f"Hello {args.name}")

if __name__ == "__main__":
    main()

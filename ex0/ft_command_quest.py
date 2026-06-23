#!usr/bin/venv python3
import sys


def main(args: list[str]) -> None:
    print(f"Program name: {args[0]}")

    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main(sys.argv)

#!usr/bin/venv python3
import sys


def ft_score_analytics(args: list[str]) -> None:

    new: list[int] = []
    for arg in args:
        try:
            new.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: {arg}")
    if len(new) == 0:
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {new}")
        print(f"Total players: {len(new)}")
        print(f"Total score: {sum(new)}")
        print(f"Avarage score: {round(sum(new) / len(new), 1)}")
        print(f"High score: {max(new)}")
        print(f"Low score: {min(new)}")
        print(f"Score range: {max(new) - min(new)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
    else:
        ft_score_analytics(sys.argv[1::])

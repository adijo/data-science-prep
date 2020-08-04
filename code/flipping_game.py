import random


def flipping_game() -> bool:
    """
    :return: True if I win the game
    """
    flips = ["H", "T"]
    prev_flip = random.choice(flips)
    while True:
        curr_flip = random.choice(flips)
        if prev_flip == "H" and curr_flip == "H":
            return True
        elif prev_flip == "T" and curr_flip == "H":
            return False
        prev_flip = curr_flip


def main():
    n_experiments = 10000
    n_wins = 0
    for _ in range(n_experiments):
        if flipping_game():
            n_wins += 1
    return n_wins / float(n_experiments)


if __name__ == "__main__":
    print(main())

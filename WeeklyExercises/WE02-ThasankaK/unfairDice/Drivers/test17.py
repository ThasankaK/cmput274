# By Ali Gharari, Paul Lu
# Assumes unfairDice.py, or symbolic link is in current working directory

import unfairDice
import sys


if __name__ == "__main__":
    print("*************************************************", file=sys.stderr)
    print("test17", file=sys.stderr)
    rolls = [1,2,1,1,2]
    unfairDice.draw_histogram(2, rolls, 0)

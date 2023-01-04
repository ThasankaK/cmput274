# By Ali Gharari, Paul Lu
# Assumes unfairDice.py, or symbolic link is in current working directory

import unfairDice
import sys

if __name__ == "__main__":
    print("*************************************************", file=sys.stderr)
    print("test3", file=sys.stderr)
    prob_list = [1/12, 1/8, 1/16, 1/16, 1/3, 1/12, 1/12, 1/6]
    seed = 2**32-1
    n=10000
    print(unfairDice.biased_rolls(prob_list, seed, n))

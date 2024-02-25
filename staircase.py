#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    stairs = []
    for level in range(n):
        spaces = " " * ((n - level) - 1)
        steps = "#" * (level + 1)
        stairs.append([spaces + steps])

    return stairs


if __name__ == "__main__":
    n = int(input().strip())

    result = staircase(n)
    for level in result:
        print("".join(map(str, level)))

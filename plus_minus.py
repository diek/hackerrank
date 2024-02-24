#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plus_minus(arr):
    # Write your code here
    pos = []
    neg = []
    zero = []
    positive_ratio = negative_ratio = zero_ratio = 0.0

    for num in arr:
        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)
        elif num == 0:
            zero.append(num)

    positive_ratio = len(pos) / n
    negative_ratio = len(neg) / n
    zero_ratio = len(zero) / n

    return [positive_ratio, negative_ratio, zero_ratio]


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)

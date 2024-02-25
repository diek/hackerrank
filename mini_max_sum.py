#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def mini_max_sum(arr):
    # Write your code here
    max = 0
    min = arr[0]
    idx_min = idx_max = 0

    for idx, num in enumerate(arr):
        if num < min:
            min = num
            idx_min = idx
        elif num > max:
            max = num
            idx_max = idx

    mini_sum = arr.copy()
    max_sum = arr.copy()
    mini_sum.pop(idx_max)
    max_sum.pop(idx_min)
    return [sum(mini_sum), sum(max_sum)]


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    mini_max = mini_max_sum(arr)
    print(f"{mini_max[0]} {mini_max[1]}")

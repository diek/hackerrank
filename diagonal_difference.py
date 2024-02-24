#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonal_difference(arr):
    x = list(range(3))
    y = x[:]
    y.reverse()
    x_sum = y_sum = 0

    for num_x, num_y in zip(x, y):
        x_sum += arr[num_x][num_x]
        y_sum += arr[num_x][num_y]
    return abs(x_sum - y_sum)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    sum = 0
    for num in ar:
        sum += num
    print(sum)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # ar_count = int(input().strip())
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    # ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + "\n")

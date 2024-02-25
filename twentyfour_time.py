#!/bin/python3

import math
import os
import random
import re
import sys
from randomtimestamp import random_time

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def time_conversion(s):
    time = s[:-2]
    hour = int(time[0:2])
    minutes_seconds = time[3:]
    if "PM" == s[-2:]:
        if hour == 12:
            return str(hour) + ":" + minutes_seconds
        else:
            hour += 12
            return str(hour) + ":" + minutes_seconds
    else:
        if hour == 12:
            return "00:" + minutes_seconds
        elif hour < 10:
            return "0" + str(hour) + ":" + minutes_seconds
        else:
            return str(hour) + ":" + minutes_seconds


def gen_time():
    return random_time(text=True, pattern="%I:%M:%S%p")


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # s = input()
    for twelve_hr in range(35):
        sample_time = gen_time()
        print(time_conversion(sample_time))

    # fptr.write(result + "\n")

    # fptr.close()

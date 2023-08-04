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
    m= " "
    t =1
    while n > n-n:
        print((n-1)*m+t*("#"))
        n=n-1
        t = t+1
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

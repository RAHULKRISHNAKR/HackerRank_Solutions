'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.'''

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

def plusMinus(arr):
    # Write your code here
    n=len(arr)
    pos=0.0
    neg=0.0
    zero=0.0
    for num in  arr:
        if num>0:
            pos+=1
        elif(num<0):
            neg+=1
        else:
            zero+=1 
    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

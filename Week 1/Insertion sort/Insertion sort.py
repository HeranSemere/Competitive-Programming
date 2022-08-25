#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    newArr = arr
    last = arr[n-1]
    for i in range(0, n-1)[::-1]:
        if arr[i] > last :
            newArr[i+1] = arr[i]
            print(' '.join(map(str, newArr)))
            if(i==0):
                newArr[i] = last
                print(' '.join(map(str, newArr)))
            
        else:
            newArr[i+1] = last
            print(' '.join(map(str, newArr)))
            return 
    
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

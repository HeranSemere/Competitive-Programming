#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    
    zero_list = [0]*100
    for i in range(0,len(arr)):
        zero_list[arr[i]] = zero_list[arr[i]]+1
        
    return zero_list



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

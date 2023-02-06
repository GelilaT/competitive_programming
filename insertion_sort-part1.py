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
    # Write your code here
    to_be_compared=arr[n-1]
    index=n-2
    while arr[index] > to_be_compared and index >= 0:
        arr[index+1]=arr[index]
        print(*arr)
        index-=1
    arr[index+1]=to_be_compared
    print(*arr)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

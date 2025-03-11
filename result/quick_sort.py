import time
import random
import sys

sys.setrecursionlimit(100000) 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    elem = arr[0]
    left = [x for x in arr if x < elem]
    center = [x for x in arr if x == elem]
    right = [x for x in arr if x > elem]


    return quick_sort(left) + center + quick_sort(right)


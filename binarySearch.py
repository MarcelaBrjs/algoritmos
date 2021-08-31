import random
import math


def binarySearch(array, k):
    n = len(array)
    left = 0
    right = n - 1

    while left <= right:
        m = math.floor((left + right) / 2)
        if k == array[m]:
            return m
        elif k < array[m]:
            right = m - 1
        else:
            left = m + 1
    return -1


values = []
for i in range(1, 10):
    values.append(random.randint(1, 10))
print(values)
print(binarySearch(values, 3))

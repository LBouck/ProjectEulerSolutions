import time

import numpy as np

import itertools


def num_divisors(num):
    divisor_candidates = np.arange(1, int(np.sqrt(num+1))+1)
    return 2*divisor_candidates[num % divisor_candidates == 0].size


def first_triangle_with_ndivisors(n):
    for num in itertools.count(1):
        if num_divisors(num*(num+1)/2) > n:
            return int(num*(num+1)/2)


t0 = time.time()
answer = first_triangle_with_ndivisors(500)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))

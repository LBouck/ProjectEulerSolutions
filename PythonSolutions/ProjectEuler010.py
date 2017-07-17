import time

import numpy as np


def is_prime(num):
    for i in range(2, int(np.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


def sum_primes_below(n):
    sum_of_primes = 0
    for num in range(2, n):
        if is_prime(num):
            sum_of_primes += num
    return sum_of_primes


t0 = time.time()
answer = sum_primes_below(2000000)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))

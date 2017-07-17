import time
import numpy as np

def largest_prime_factor(n):
    for x in range(2,n):
        if n%x==0:
            return largest_prime_factor(n/x)
    return n


t0 = time.time()
answer = largest_prime_factor(600851475143)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))
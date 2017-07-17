import time
import numpy as np

def is_prime(num):
    for i in range(2,int(np.sqrt(num)+1)):
        if num%i==0:
            return False
    return True
def nth_prime(n):
    count = 0
    num = 2
    factors = 0
    while count<=n:
        if is_prime(num):
            count += 1
        num += 1
    return num
t0 = time.time()
answer = nth_prime(10001)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))
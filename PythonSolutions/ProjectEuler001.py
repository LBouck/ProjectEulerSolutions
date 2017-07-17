#project euler 001
import numpy as np
import time
t0 = time.time()

# create array of values up to 1000
arr = np.arange(1,1000)
sum = np.sum(arr[np.logical_or(arr%3==0, arr%5==0)])

t1 = time.time()

print("Sum is: "+str(sum))
print("Time elapsed is: "+str(t1-t0))

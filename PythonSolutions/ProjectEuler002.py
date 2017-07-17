
import time
t0 = time.time()
sum = 0
fib1 = 0
fib2 = 1
temp = 0
while fib2<4000000:
    temp = fib1+fib2
    fib1 = fib2
    fib2 = temp
    if fib2%2==0:
        sum += fib2
t1 = time.time()

print("Sum is: "+str(sum))
print("Time elapsed is: "+str(t1-t0))
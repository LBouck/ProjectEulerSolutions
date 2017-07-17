import time

def square_of_sum(num):
    return (num*(num+1)//2)**2

def sum_of_squares(num):
    return num*(num+1)*(2*num+1)/6

t0 = time.time()
answer = square_of_sum(100)-sum_of_squares(100)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))
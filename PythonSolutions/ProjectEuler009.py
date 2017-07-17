import time

def is_pythagorean_triplet(a,b,c):
    return a**2+b**2-c**2==0

def find_tripletProduct_addsto(n):
    for b in range(1,n):
        for a in range(1,b):
            c = n-a-b
            if is_pythagorean_triplet(a,b,c):
                return a*b*c
t0 = time.time()
answer = find_tripletProduct_addsto(1000)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))
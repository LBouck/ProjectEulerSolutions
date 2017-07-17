import time


def largest_palindrome_product(digits):
    max = 0
    candidate = 0
    start = 10**(digits-1)
    end = 10**digits

    for i in range(start,end):
        for j in range(i,end):
            candidate = i*j
            if (is_palindrome(candidate) and candidate>max):
                max = candidate
    return max

def nthdigit(n, num):
    if (n==1):
        return num%(10**n)
    else:
        return int((num%(10**n)-num%(10**(n-1)))/(10**(n-1)))

def is_palindrome(num):
    digits = 0
    while (num%(10**digits)!=num):
        digits += 1
    for n in range(1, int(digits/2)+1):
        if (nthdigit(n,num)!=nthdigit(digits-n+1,num)):
            return False
    return True



t0 = time.time()
answer = largest_palindrome_product(3)
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))
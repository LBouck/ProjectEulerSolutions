import time

def prime_factorization(num):
    prime_factors = []
    for i in range(2, num):
        if num%i==0:
            prime_factors += prime_factorization(num//i)+prime_factorization(i)
            return prime_factors
    prime_factors.append(num)
    return prime_factors

def scalar_lcm(x,y):
    x_factors = prime_factorization(x)
    y_factors = prime_factorization(y)

    taken_care = []
    least_mult = 1

    for p in x_factors:
        if p not in taken_care:
            least_mult *= p**max([x_factors.count(p),y_factors.count(p)])
            taken_care.append(p)
    for p in y_factors:
        if p not in taken_care:
            least_mult *= p**max([x_factors.count(p), y_factors.count(p)])

    return least_mult

def lcm(num_list):
    if len(num_list)==2:
        return scalar_lcm(num_list[0], num_list[1])
    else:
        return scalar_lcm(lcm(num_list[:-1]),num_list[-1])




t0 = time.time()
answer = lcm(range(2,21))
t1 = time.time()

print("Answer is: "+str(answer))
print("Time elapsed is: "+str(t1-t0))
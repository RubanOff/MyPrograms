import math

# Fibonachi generator
def genFibonachi(n = None):
    a = 1
    b = 1
    count = 0
    while n is None or count < n:
        yield a
        a, b = b, a + b
        count += 1


for num in genFibonachi(10):
    print(num)


# =====================================================================
# Prime numbers genarator
def GenPrimeNumbers(n = None):
    a = 2
    while n is None or a <= n:
        if is_prime(a):
            yield a
        a +=1


# Check on prime number
def is_prime(a):
    if a == 1:
        return False
    for d in range(2, int(math.sqrt(a)) + 1):
        if a % d == 0:
            return False
    return True


for num in GenPrimeNumbers(11):
    print(num)


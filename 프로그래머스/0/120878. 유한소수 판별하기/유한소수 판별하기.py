import math

def solution(a, b):
    gcd = math.gcd(a, b)
    a, b = a // gcd, b // gcd

    if a == b:
        return 1
    else:
        arr = []
        for i in range(2, b+1):
            while b % i == 0:
                b //= i
                arr.append(i)
        if all(n in (2, 5) for n in arr):
            return 1
        else:
            return 2
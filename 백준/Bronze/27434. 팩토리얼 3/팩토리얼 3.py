import sys
sys.setrecursionlimit(10**6)

N = int(input())

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

print(fac(N))
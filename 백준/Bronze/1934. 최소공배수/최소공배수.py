import math

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    lcm = (A*B)//gcd
    print(lcm)
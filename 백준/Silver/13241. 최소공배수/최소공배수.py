import math

A, B = map(int, input().split())
gcd = math.gcd(A, B)
res = (A * B) // gcd


print(res)
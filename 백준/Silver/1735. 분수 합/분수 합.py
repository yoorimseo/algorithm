import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

res1 = a1 * b2 + a2 * b1
res2 = b1 * b2

_gcd = math.gcd(res1, res2)

res1 //= _gcd
res2 //= _gcd

print(res1, res2)
import sys

Q = int(sys.stdin.readline())
for _ in range(Q):
    a = int(sys.stdin.readline())
    print(repr(0 if (a & (a - 1)) else 1))
import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
F = Counter(A)
NGF = [-1] * N
stack = []

for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]

    stack.append(i)

print(*NGF)
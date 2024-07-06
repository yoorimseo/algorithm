import sys
input = sys.stdin.readline
N, M = map(int, input().split())
H = list(map(int, input().split()))

diff = [0] * (N + 1)

for _ in range(M):
    a, b, k = map(int, input().split())
    diff[a-1] += k
    if b < N:
        diff[b] -= k

current_addition = 0
for i in range(N):
    current_addition += diff[i]
    H[i] += current_addition

print(*H)
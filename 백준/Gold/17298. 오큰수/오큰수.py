import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

NGE = [-1] * N
idx = []

for i in range(N):
    while idx and arr[idx[-1]] < arr[i]:
        NGE[idx.pop()] = arr[i]

    idx.append(i)

print(' '.join(map(str, NGE)))
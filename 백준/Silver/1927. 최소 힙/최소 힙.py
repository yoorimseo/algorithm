import sys
import heapq

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(arr):
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, num)
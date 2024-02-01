import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x:
        heapq.heappush(heap, -x)
    else:
        if len(heap):
            temp = heapq.heappop(heap)
            print(-temp)
        else:
            print(0)
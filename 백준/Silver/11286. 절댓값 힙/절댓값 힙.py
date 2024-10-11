import sys, heapq

N = int(sys.stdin.readline())
abs_heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(x), x))
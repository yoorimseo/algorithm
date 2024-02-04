import heapq

N = int(input())
heap = []

for _ in range(N):
    num = list(map(int, input().split()))
    for i in num:
        if len(heap) < N:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heap[0])
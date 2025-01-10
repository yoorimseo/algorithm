import heapq

N = int(input())
lecture = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[1])

heap = []
cnt = 0

for i in lecture:
    while heap and heap[0] <= i[1]:
        heapq.heappop(heap)

    heapq.heappush(heap, i[2])
    cnt = max(cnt, len(heap))

print(cnt)
import heapq

N, H, T = map(int, input().split())
heap = [-int(input()) for _ in range(N)]
heapq.heapify(heap)
cnt = 0

for _ in range(T):
    height = -heapq.heappop(heap)
    if height == 1 or height < H:
        heapq.heappush(heap, -height)
        break
    else:
        heapq.heappush(heap, -(height // 2))
        cnt += 1

if -heap[0] >= H:
    print('NO', -heap[0], sep='\n')
else:
    print('YES', cnt, sep='\n')

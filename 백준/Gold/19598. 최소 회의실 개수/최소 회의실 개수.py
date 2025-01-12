import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
rooms = []
cnt = 0

for i in arr:
    start, end = i[0], i[1]

    if rooms and rooms[0] <= start:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    else:
        heapq.heappush(rooms, end)
        cnt += 1

print(cnt)
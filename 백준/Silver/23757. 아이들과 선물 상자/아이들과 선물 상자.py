import heapq

N, M = map(int, input().split())
gifts = []
for i in list(map(int, input().split())):
    heapq.heappush(gifts, -i)
wants = list(map(int, input().split()))

res = 1

for j in wants:
    temp = -heapq.heappop(gifts)

    if temp - j < 0:
        res = 0
        break
    heapq.heappush(gifts, -(temp - j))

print(res)
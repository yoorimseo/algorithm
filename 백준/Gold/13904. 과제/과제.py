import heapq

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort()

res = []

for i in range(N):
    heapq.heappush(res, arr[i][1])

    if arr[i][0] < len(res):
        heapq.heappop(res)

print(sum(res))
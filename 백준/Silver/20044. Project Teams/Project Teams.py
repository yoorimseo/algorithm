import heapq

n = int(input())
w = list(map(int, input().split()))
w.sort(reverse=True)
g = []

for i in range(n):
    heapq.heappush(g, (w[i], w[len(w) - (i + 1)]))

res = []

for j in g:
    res.append(sum(j))

print(min(res))
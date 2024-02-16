N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
min_cost = costs[0]

for i in range(N-1):
    if costs[i] < min_cost:
        min_cost = costs[i]

    res += min_cost * roads[i]

print(res)
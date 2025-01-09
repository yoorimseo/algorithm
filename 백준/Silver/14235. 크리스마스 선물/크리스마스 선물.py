import heapq

n = int(input())
gift = []

for _ in range(n):
    inp = list(map(int, input().split()))
    a = inp[0]

    if len(inp) < 2:
        if a == 0:
            if len(gift) == 0:
                print(-1)
            else:
                print(-heapq.heappop(gift))
    else:
        for i in range(a):
            heapq.heappush(gift, -inp[i+1])
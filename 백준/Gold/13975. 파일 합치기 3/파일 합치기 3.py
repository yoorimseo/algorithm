import heapq

T = int(input())

for _ in range(T):
    K = int(input())

    file_sizes = list(map(int, input().split()))
    heapq.heapify(file_sizes)

    res = 0

    while len(file_sizes) > 1:
        temp = 0
        x = heapq.heappop(file_sizes)
        y = heapq.heappop(file_sizes)

        temp += x + y
        res += temp

        heapq.heappush(file_sizes, temp)

    print(res)
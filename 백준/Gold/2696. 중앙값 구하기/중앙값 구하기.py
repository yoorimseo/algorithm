import heapq

T = int(input())

for _ in range(T):
    M = int(input())
    arr = []
    for _ in range((M-1) // 10 + 1):
        arr += list(map(int, input().split()))

    max_heap = []
    min_heap = []
    res = []

    for i in range(M):
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -arr[i])
        else:
            heapq.heappush(min_heap, arr[i])

        if min_heap and min_heap[0] < -max_heap[0]:
            max_value = heapq.heappop(max_heap)
            min_value = heapq.heappop(min_heap)

            heapq.heappush(max_heap, -min_value)
            heapq.heappush(min_heap, -max_value)

        if i % 2 == 0:
            res.append(-max_heap[0])

    print(len(res))
    for i in range(0, len(res), 10):
        print(*res[i:i+10])
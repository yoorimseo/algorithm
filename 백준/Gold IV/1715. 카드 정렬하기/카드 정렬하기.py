import sys
import heapq

N = int(sys.stdin.readline())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

res = 0

while len(cards) > 1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    res += A + B
    heapq.heappush(cards, A+B)

print(res)
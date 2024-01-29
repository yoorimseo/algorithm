from collections import deque

N = int(input())
card = deque(range(1, N+1))
res = []

while len(card) > 0:
    delete = card.popleft()
    res.append(delete)
    if len(card) != 0:
        tmp = card.popleft()
        card.append(tmp)

print(*res)
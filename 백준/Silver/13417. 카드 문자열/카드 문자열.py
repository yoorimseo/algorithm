from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    cards = list(input().split())
    sort_cards = deque()
    sort_cards.append(cards[0])
    cmp = cards[0]

    for i in range(1, len(cards)):
        if cards[i] <= cmp:
            sort_cards.appendleft(cards[i])
            cmp = cards[i]
        else:
            sort_cards.append(cards[i])

    print(''.join(sort_cards))
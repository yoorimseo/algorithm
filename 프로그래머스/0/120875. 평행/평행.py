from itertools import combinations

def solution(dots):
    for a, b in combinations(combinations(dots, 2), 2):
        x = set(tuple(i) for i in a)
        y = set(tuple(i) for i in b)
        if x.isdisjoint(y):
            x = list(x)
            y = list(y)
            a1 = abs(x[0][1] - x[1][1]) / abs(x[0][0] - x[1][0])
            a2 = abs(y[0][1] - y[1][1]) / abs(y[0][0] - y[1][0])
            if a1 == a2:
                return 1

    return 0
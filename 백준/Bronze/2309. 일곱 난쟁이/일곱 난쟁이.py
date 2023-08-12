import itertools

arr = [int(input()) for _ in range(9)]

for i in itertools.combinations(arr, 7):
    if sum(i) == 100:
        res = list(i)
        res.sort()
        print(*res, sep='\n')
        break
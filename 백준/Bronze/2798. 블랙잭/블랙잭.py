from itertools import combinations

N, M = map(int, input().split())
num = list(map(int, input().split()))
max_num = 0

for i in combinations(num, 3):
    sum_num = sum(i)
    if max_num < sum_num <= M:
        max_num = sum_num

print(max_num)
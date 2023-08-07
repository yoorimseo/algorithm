N = int(input())
level = list(map(int, input().split()))
level.sort(reverse=True)
gold = 0
max_level = level[0]

for i in range(1, len(level)):
    gold += (max_level + level[i])

print(gold)
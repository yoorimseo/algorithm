h, w = map(int, input().split())
world = list(map(int, input().split()))
res = 0

for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        res += compare - world[i]

print(res)
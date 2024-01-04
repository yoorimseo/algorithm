N, C = map(int, input().split())
M = int(input())
box = [list(map(int, input().split())) for _ in range(M)]
box.sort(key=lambda x: x[1])
contain = [C] * (N + 1)
res = 0

for i in box:
    min_box = C

    for j in range(i[0], i[1]):
        min_box = min(min_box, contain[j])

    min_box = min(min_box, i[2])

    for k in range(i[0], i[1]):
        contain[k] -= min_box

    res += min_box

print(res)
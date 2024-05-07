N = int(input())
array = [[0] * 100 for _ in range(100)]

for _ in range(N):
    y, x = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1

result = 0
for k in range(100):
    result += array[k].count(1)

print(result)

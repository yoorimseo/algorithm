N = int(input())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
ans = [0, 0]

def dac(i, j, n):
    color = arr[i][j]
    for y in range(i, i + n):
        for x in range(j, j + n):
            if color != arr[y][x]:
                quarter = n // 2
                dac(i, j, quarter)
                dac(i, j + quarter, quarter)
                dac(i + quarter, j, quarter)
                dac(i + quarter, j + quarter, quarter)
                return
    ans[color] += 1

dac(0, 0, N)

print(ans[0])
print(ans[1])
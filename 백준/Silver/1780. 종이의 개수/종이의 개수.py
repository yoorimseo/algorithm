N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = [0] * 3

def search(x, y, n):
    global res
    check = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        search(x+k*n//3, y+l*n//3, n//3)
                return

    if check == -1:
        res[0] += 1
    elif check == 0:
        res[1] += 1
    else:
        res[2] += 1

search(0, 0, N)
print(*res, sep='\n')
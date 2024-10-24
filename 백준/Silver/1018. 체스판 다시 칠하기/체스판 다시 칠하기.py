N, M = map(int, input().split())
board = [input() for _ in range(N)]
count = []

for col in range(N-7):
    for row in range(M-7):
        index1 = index2 = 0
        for i in range(col, col+8):
            for j in range(row, row+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
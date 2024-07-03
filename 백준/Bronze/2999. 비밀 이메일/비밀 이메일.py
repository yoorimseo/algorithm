msg = input()
N = len(msg)
x, y = 0, 0

for i in range(1, N//2 + 1):
    for j in range(i, N+1):
        if i * j == N:
            x, y = i, j

for i in range(x):
    for j in range(y):
        print(msg[i + j * x], end='')
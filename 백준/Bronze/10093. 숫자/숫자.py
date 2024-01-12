A, B = map(int, input().split())
X = min(A, B)
Y = max(A, B)
arr = list(range(X+1, Y))

if len(arr) != 0:
    print(len(arr))
    print(*arr)
else:
    print(len(arr))
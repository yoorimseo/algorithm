X, Y = input().split()
res = int(X[::-1]) + int(Y[::-1])
revRes = str(res)[::-1]

print(int(revRes))
N, L = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for h in fruits:
    if h <= L:
        L += 1

print(L)
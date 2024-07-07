S = input()
q = int(input())

for _ in range(q):
    a, l, r = input().split(' ')
    l, r = int(l), int(r)
    res = list(filter(lambda s: s == a, S[l:r+1]))

    print(len(res))

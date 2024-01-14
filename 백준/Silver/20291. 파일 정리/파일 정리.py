N = int(input())
dict = {}

for _ in range(N):
    file = input().split('.')

    if file[1] not in dict:
        dict[file[1]] = 1
    else:
        dict[file[1]] += 1

res = sorted(dict.items())

for i in res:
    print(*i)
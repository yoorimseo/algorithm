n = int(input())
arr = []

for _ in range(n):
    inp = input().split()
    name = inp[0]
    state = inp[1]

    if state == 'enter':
        arr.append(name)
    else:
        arr.remove(name)

arr.sort(reverse=True)

print(*arr, sep='\n')
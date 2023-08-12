cnt = 0

for i in range(8):
    arr = list(input())
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and arr[j] == 'F':
            cnt += 1
        elif i % 2 == 1 and j % 2 == 1 and arr[j] == 'F':
            cnt += 1

print(cnt)
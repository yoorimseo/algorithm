N = int(input())
arr = []

for i in range(1, N+1):
    if str(i).count('3') or str(i).count('6') or str(i).count('9'):
        cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
        arr.append('-'*cnt)
    else:
        arr.append(i)

print(*arr)
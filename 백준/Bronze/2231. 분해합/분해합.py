N = int(input())
res = 0

for i in range(1, N):
    tmp = i
    for digit in str(i):
        tmp += int(digit)
    
    if tmp == N:
        res = i
        break

print(res)

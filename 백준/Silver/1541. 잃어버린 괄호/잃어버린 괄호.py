arr = input().split('-')
res = sum(list(map(int, arr[0].split('+'))))

for i in arr[1:]:
    if '+' in i:
        res -= sum(list(map(int, i.split('+'))))
    else:
        res -= int(i)

print(res)
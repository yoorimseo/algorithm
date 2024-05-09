for i in range(1, 11):
    length = int(input())
    arr = input()
    res = 0
    
    for j in arr:
        if j.isdigit():
            res += int(j)
    
    print(f'#{i} {res}')
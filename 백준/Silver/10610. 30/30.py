N = list(input())
N = sorted(N, reverse=True)

if N[-1] != '0':
    print(-1)
else:
    res = 0
    
    for i in N:
        res += int(i)
        
    if res % 3 != 0:
        print(-1)
    else:
        print(''.join(N))
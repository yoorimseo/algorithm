N = list(map(int, input()))
L = N[:len(N)//2]
R = N[len(N)//2:]

if sum(L) == sum(R):
    print('LUCKY')
else:
    print('READY')
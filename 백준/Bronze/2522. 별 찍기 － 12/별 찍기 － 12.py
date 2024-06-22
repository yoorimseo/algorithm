N = int(input())
arr = [' '] * N
for i in range(1, N*2):
    if i < N+1:
        arr[N-i] = '*'
    else:
        arr[i-N-1] = ' '

    print(''.join(arr))
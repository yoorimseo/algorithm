N = int(input())
arr = [str(i) for i in range(1, N+1)]
new_N = ''.join(arr)

print(new_N.index(str(N))+1)
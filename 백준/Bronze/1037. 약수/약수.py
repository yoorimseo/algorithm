N = int(input())
arr = sorted(list(map(int, input().split())))

if len(arr) > 1:
    print(arr[0] * arr[-1])
else:
    print(arr[0] * arr[0])
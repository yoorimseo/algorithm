T = int(input())

for _ in range(T):
    arr = sorted(list(map(int, input().split())), reverse=True)
    print(arr[2])
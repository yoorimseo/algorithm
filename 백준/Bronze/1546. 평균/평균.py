N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
res = sum(list(map(lambda x: x / M * 100, arr))) / N

print(res)
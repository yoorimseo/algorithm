n = int(input())
numbers = list(map(int, input().split()))
arr = [0]

for x in numbers:
	arr.append(x - arr[-1])

min_num = -min(arr[::2])
max_num = min(arr[1::2])
res = max(0, max_num-min_num+1)

print(res)
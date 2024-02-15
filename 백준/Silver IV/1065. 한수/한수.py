N = int(input())
cnt = 0

for n in range(1, N+1):
    if n <= 99:
        cnt += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            cnt += 1

print(cnt)
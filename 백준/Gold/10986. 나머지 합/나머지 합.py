N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = 0
cnt_mod = [0] * M
cnt_mod[0] = 1
res = 0

for i in arr:
    sum_arr = (sum_arr + i) % M
    res += cnt_mod[sum_arr]
    cnt_mod[sum_arr] += 1

print(res)
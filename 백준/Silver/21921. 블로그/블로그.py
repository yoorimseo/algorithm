N, X = map(int, input().split())
visitors = list(map(int, input().split()))
sw = sum(visitors[:X])
max_sum = sw
max_cnt = 1

for i in range(X, N):
    sw -= visitors[i-X]
    sw += visitors[i]

    if sw == max_sum:
        max_cnt += 1
    elif max_sum < sw:
        max_sum = sw
        max_cnt = 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum, max_cnt, sep='\n')
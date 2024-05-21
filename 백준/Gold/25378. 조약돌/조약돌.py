N = int(input())
stone = list(map(int, input().split()))
stone_cnt = [[s] for s in stone]
cnt = N

for i in range(1, N):
    for sc in stone_cnt[i-1]:
        if sc < stone[i]:
            stone_cnt[i].append(stone[i] - sc)
        elif sc == stone[i]:
            stone_cnt[i] = []
            cnt -= 1
            break
print(cnt)
N = int(input())
score = []
cnt = 0

for _ in range(N):
    score.append(int(input()))

for i in reversed(range(N - 1)):
    cmp = score[i + 1]

    while cmp <= score[i]:
        score[i] -= 1
        cnt += 1

print(cnt)
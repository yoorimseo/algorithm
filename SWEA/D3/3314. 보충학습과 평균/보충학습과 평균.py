T = int(input())

for i in range(T):
    scores = list(map(int, input().split()))

    for j in range(len(scores)):
        if scores[j] < 40:
            scores[j] = 40

    avg = sum(scores) // 5
    print(f'#{i+1} {avg}')
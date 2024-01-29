K = int(input())

for i in range(K):
    inp = list(map(int, input().split()))
    N = inp[0]
    score = inp[1:]
    max_score, min_score = max(score), min(score)
    score.sort(reverse=True)
    gap = 0

    for j in range(1, len(score)):
        if gap < score[j-1] - score[j]:
            gap = score[j-1] - score[j]

    print(f'Class {i+1}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')
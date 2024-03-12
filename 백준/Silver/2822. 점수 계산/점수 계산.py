scores = [int(input()) for _ in range(8)]
sort_scores = sorted(scores, reverse=True)
res = sum(sort_scores[:5])
index = []

for i in sort_scores[:5]:
    idx = scores.index(i) + 1
    index.append(idx)

index.sort()

print(res)
print(*index)
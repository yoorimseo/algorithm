N = int(input())
target = input().strip()
words = [input().strip() for _ in range(N - 1)]
cnt = 0

for word in words:
    if abs(len(target) - len(word)) > 1 or len(set(target).difference(set(word))) > 1:
        continue

    for i in target:
        word = word.replace(i, '', 1)

    if len(word) <= 1:
        cnt += 1

print(cnt)

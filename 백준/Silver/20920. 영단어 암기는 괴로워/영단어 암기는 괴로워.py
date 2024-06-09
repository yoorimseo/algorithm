import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []

for _ in range(N):
    s = input().strip()
    if len(s) >= M:
        words.append(s)

frequency = dict()
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_words = sorted(frequency.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

res = [item[0] for item in sorted_words]
print(*res, sep='\n')
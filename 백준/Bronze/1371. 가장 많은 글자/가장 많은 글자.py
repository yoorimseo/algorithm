import sys

input = sys.stdin.read
string = input().replace('\n', '').replace(' ', '')

cnt = [0] * 26
for i in string:
    cnt[ord(i) - ord('a')] += 1

res = []
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        res.append(chr(i + ord('a')))

res.sort()
print(*res, sep='')
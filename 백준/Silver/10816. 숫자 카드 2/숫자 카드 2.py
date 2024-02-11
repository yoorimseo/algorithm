import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))
_dict = {}

for i in cards:
    if i not in _dict:
        _dict[i] = 1
    else:
        _dict[i] += 1

for j in checks:
    if j in _dict:
        print(_dict[j], end=' ')
    else:
        print(0, end=' ')
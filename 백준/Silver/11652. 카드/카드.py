N = int(input())
nums = [int(input()) for _ in range(N)]
_dict = dict()

for n in nums:
    if n not in _dict:
        _dict[n] = 1
    else:
        _dict[n] += 1

res = sorted(_dict.items(), key=lambda item: (-item[1], item[0]))
print(res[0][0])
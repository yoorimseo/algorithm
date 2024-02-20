N = int(input())
_dict = dict()

for _ in range(N):
    book = input()

    if book not in _dict:
        _dict[book] = 1
    else:
        _dict[book] += 1

max_sell_name = ''
max_sell_cnt = 0

for i in _dict:
    if _dict[i] > max_sell_cnt:
        max_sell_name = i
        max_sell_cnt = _dict[i]
    elif _dict[i] == max_sell_cnt:
        cmp = sorted([i, max_sell_name])
        max_sell_name = cmp[0]

print(max_sell_name)
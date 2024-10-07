arr = []
_dict = dict()

for _ in range(10):
    n = int(input())
    arr.append(n)

    if n not in _dict:
        _dict[n] = 1
    else:
        _dict[n] += 1

sort_dict = sorted(_dict.items(), key=lambda x: x[1], reverse=True)

print(sum(arr) // 10)
print(sort_dict[0][0])
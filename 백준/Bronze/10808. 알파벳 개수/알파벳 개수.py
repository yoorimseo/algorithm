line = input()
res = [0] * 26

for i in line:
    idx = ord(i) - 97
    res[idx] += 1

print(*res)
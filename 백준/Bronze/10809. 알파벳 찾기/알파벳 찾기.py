line = input()
res = [-1] * 26

for i in range(26):
    if chr(i + 97) in line:
        res[i] = line.index(chr(i + 97))

print(*res)
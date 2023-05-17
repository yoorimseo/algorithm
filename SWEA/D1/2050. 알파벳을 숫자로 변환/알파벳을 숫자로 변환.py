str = list(input());
res = [];

for s in str:
    res.append(ord(s) - 64);

print(*res);
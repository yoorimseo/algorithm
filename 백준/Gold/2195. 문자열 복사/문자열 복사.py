S = input()
P = input()
idx = 0
res = 1

for i in range(len(P)):
    if S.find(P[idx:i + 1]) >= 0:
        continue
    idx = i
    res += 1

print(res)
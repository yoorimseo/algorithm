N = int(input())
info = []

for _ in range(N):
    inp = list(input().split())
    info.append([inp[0], int(inp[1]), int(inp[2]), int(inp[3])])

info.sort(key=lambda x: (x[3], x[2], x[1]))
print(info[-1][0], info[0][0], sep='\n')
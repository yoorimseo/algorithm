N, M = map(int, input().split())
A = set(input() for _ in range(N))
B = set(input() for _ in range(M))
res = sorted(list(A & B))

print(len(res))
print(*res, sep='\n')
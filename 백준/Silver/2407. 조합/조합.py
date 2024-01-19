N, M = map(int, input().split())
x = 1
y = 1

for i in range(N-M+1, N+1):
    x *= i

for j in range(1, M+1):
    y *= j

print(x//y)
N = int(input())
clap = 0

for i in range(1, N+1):
    for j in '369':
        clap += str(i).count(j)

print(clap)
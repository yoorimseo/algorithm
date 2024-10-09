N = int(input())
lengths = sorted([int(input()) for _ in range(N)], reverse=True)

for i in range(len(lengths)-2):
    if sum(lengths[i+1:i+3]) > lengths[i]:
        print(sum(lengths[i:i+3]))
        break
else:
    print(-1)
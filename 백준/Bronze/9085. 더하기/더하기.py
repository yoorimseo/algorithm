T = int(input())

for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    res = list(filter(lambda x: x <= 10, num))
    print(sum(res))
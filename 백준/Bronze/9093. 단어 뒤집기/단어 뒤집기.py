N = int(input())

for _ in range(N):
    words = input().split()
    res = [ i[::-1] for i in words ]

    print(' '.join(res))
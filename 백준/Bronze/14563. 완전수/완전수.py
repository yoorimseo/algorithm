T = int(input())
arr = list(map(int, input().split()))

for n in arr:
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        print('Perfect')
    elif total > n:
        print('Abundant')
    else:
        print('Deficient')
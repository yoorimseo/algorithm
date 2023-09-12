N = int(input())
zero = 0
one = 0

for _ in range(N):
    n = int(input())

    if n == 0:
        zero += 1
    else:
        one += 1

print('Junhee is not cute!' if zero > one else 'Junhee is cute!')
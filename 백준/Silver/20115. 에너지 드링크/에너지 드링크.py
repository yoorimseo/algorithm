N = int(input())
amount = list(map(int, input().split()))
amount.sort()
res = 0

while len(amount) != 1:
    amount[-1] += (amount[0] / 2)
    amount.remove(amount[0])

print(*amount)
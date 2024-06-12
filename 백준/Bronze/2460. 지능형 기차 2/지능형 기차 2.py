total, res = 0, 0

for _ in range(10):
    otp, inp = map(int, input().split())
    total += inp - otp
    res = max(res, total)

print(res)
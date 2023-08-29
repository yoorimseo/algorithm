import math

N = input()

length = len(N)
cnt = math.ceil(length / 10)
start = 0
end = 10

for _ in range(cnt):
    print(N[start:end])

    start += 10
    end += 10
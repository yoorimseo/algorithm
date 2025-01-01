N, K = map(int, input().split())

students = [[0] * 7 for _ in range(2)]

for _ in range(N):
    gender, classroom = map(int, input().split())
    students[gender][classroom] += 1

ans = 0
for gender in range(2):
    for classroom in range(1, 7):
        ans += (students[gender][classroom] + K - 1) // K

print(ans)
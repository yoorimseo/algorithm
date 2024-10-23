N = int(input())
grades = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}
total_credit = grade_average = 0

for _ in range(N):
    subject, credit, result = input().split()

    total_credit += int(credit)
    grade_average += int(credit) * grades[result]

print("%.2f" % (round(grade_average/total_credit + 10**-10, 2)))
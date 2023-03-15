import sys

lines = sys.stdin.readlines()
res = []

for line in lines:
  num = int(line.strip())
  res.append(num % 42)

print(len(set(res)))
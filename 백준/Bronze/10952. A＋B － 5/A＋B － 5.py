import sys

lines = sys.stdin.readlines()

for line in lines[:-1]:
  A, B = map(int, line.split())
  print(A + B)
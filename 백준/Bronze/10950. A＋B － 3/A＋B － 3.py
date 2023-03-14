import sys

num = int(sys.stdin.readline().strip())

for i in range(num):
  A, B = list(map(int, sys.stdin.readline().strip().split()))
  print(A + B)
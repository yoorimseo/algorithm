import sys

num = int(sys.stdin.readline().strip())

for i in range(1, 10):
  print(f'{num} * {i} = {num * i}')
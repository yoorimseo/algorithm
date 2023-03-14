import sys

num = int(sys.stdin.readline().strip())
blank = num

for i in range(1, num + 1):
  blank -= 1
  print(' ' * blank + '*' * i)
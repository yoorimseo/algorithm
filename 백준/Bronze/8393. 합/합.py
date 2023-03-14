import sys

num = int(sys.stdin.readline().strip())
res = 0

for i in range(1, num + 1):
  res += i
  
print(res)
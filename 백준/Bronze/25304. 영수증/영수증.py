import sys

total_price = int(sys.stdin.readline().strip())
total_num = int(sys.stdin.readline().strip())
res = 0

for i in range(1, total_num + 1):
  price, num = list(map(int, sys.stdin.readline().strip().split()))
  res += price * num
  
print('Yes') if res == total_price else print('No')
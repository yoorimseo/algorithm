import sys

num = int(sys.stdin.readline().strip())

for i in range(1, num + 1):
  A, B = list(map(int, sys.stdin.readline().strip().split()))
  
  print(f'Case #{i}: {A} + {B} = {A + B}')
import sys

str = sys.stdin.readline().strip()
res = []

for code in range(97, 123):
  if chr(code) in str:
    res.append(str.index(chr(code)))
  else:
    res.append(-1)
    
print(*res)
import sys

num = int(sys.stdin.readline().strip())
res = num // 4 * 'long '

print(res + 'int')
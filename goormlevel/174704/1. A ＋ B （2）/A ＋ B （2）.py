# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a, b = input().split()
res = 0

if '-' in a:
	res -= float(a[1:])
	res += float(b)
elif '-' in b:
	res -= float(b[1:])
	res += float(a)
else:
	res = float(a) + float(b)

print(f'{res:.6f}')
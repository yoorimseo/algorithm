# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a, b = input().split()

if '-' in a:
	res = - int(a[1:]) + int(b)
elif '-' in b:
	res = - int(b[1:]) + int(a)
else:
	res = int(a) + int(b)

print(res)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a, b = 0, 1
k = int(input())

if k == 1:
	print(a)

else:
	for i in range(2, k):
		a, b = b, a + b

	print(b % 1000000007)
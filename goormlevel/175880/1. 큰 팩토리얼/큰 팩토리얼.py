# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
res = 1

for i in range(1, n+1):
	res *= i
	
print(res % 1000000007)
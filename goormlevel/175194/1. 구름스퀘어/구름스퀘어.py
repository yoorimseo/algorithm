# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N = int(input())
event = []

for _ in range(N):
	s, e = map(int, input().split())
	event.append((s, e))

event.sort(key=lambda x: x[1])

count = 0
end_time = 0

for s, e in event:
	if s > end_time:
		count += 1
		end_time = e
				
print(count)
arr = [int(input()) for _ in range(7)]
odd = sorted(list(filter(lambda x: x % 2 == 1, arr)))

if len(odd):
    print(sum(odd), min(odd), sep='\n')
else:
    print(-1)
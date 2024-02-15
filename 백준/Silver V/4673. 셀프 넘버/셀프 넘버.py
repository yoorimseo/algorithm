number = list(range(1, 10001))

def self_number(n):
    num = list(str(n))
    res = n
    for n in num:
        res += int(n)
    return res

for i in range(1, 10001):
    num = self_number(i)
    if num in number:
        number.remove(num)

print(*number, sep='\n')
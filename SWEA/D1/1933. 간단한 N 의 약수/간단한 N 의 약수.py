import math;

num = int(input());
divisors = [];
sqrt_n = int(math.sqrt(num));

for i in range(1, sqrt_n + 1):
    if num % i == 0:
        divisors.append(i);
        if i != num // i:
            divisors.append(num // i);
            
divisors.sort();
print(*divisors);
from functools import reduce
import math

def solution(num_list):
    mul = reduce(lambda x, y: x * y, num_list)
    pow = math.pow(sum(num_list), 2)
    
    return 1 if mul < pow else 0
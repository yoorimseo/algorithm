def dfs(numbers, target, index, current_sum):
    if index == len(numbers):
        if current_sum == target:
            return 1
        else:
            return 0

    add = dfs(numbers, target, index + 1, current_sum + numbers[index])
    subtract = dfs(numbers, target, index + 1, current_sum - numbers[index])

    return add + subtract

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer
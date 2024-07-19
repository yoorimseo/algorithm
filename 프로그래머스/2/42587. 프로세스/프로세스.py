from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    print_order = 0

    while queue:
        current = queue.popleft()
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[0] == location:
                return print_order
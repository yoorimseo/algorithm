import heapq

def solution(jobs):
    jobs.sort()
    current, total, n = 0, 0, len(jobs)
    heap = []
    i = 0

    while i < n or heap:
        while i < n and jobs[i][0] <= current:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        if heap:
            duration, start = heapq.heappop(heap)
            total += duration + current - start
            current += duration
        else:
            current = jobs[i][0]

    return total // n
import heapq

def solution(operations):
    heap = []
    removed = []
    
    for i in operations:
        order, num = i.split(' ')
        num = int(num)
        
        if order == 'I':
            heapq.heappush(heap, num)
        elif order == 'D':
            if not heap:
                continue
            if num == 1:
                max_value = max(heap)
                heap.remove(max_value)
                heapq.heapify(heap)
            elif num == -1:
                heapq.heappop(heap)
    
    if heap:
        return [max(heap), heap[0]]
    else:
        return [0, 0]

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque()
    current_weight = 0
    truck_weights = deque(truck_weights)

    while bridge or truck_weights:
        time += 1

        if bridge and bridge[0][1] == 0:
            current_weight -= bridge.popleft()[0]

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append((truck, bridge_length))
                current_weight += truck

        for i in range(len(bridge)):
            bridge[i] = (bridge[i][0], bridge[i][1] - 1)

    return time

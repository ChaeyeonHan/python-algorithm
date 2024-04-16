# def solution(bridge_length, weight, truck_weights): # 최대 bridge_length대, weight이하의 무게
#     time = 0
#     bridge = [0] * bridge_length  # 다리길이만큼의 배열 생성
#     while len(truck_weights):
#         time += 1
#         bridge.pop(0)  # 트럭 하나가 다리를 지난다
#
#         if sum(bridge)+truck_weights[0] <= weight:
#             bridge.append(truck_weights.pop(0))
#         else:
#             bridge.append(0)  # 0을 추가해서 다리 길이를 유지
#     time += bridge_length
#
#     return time


from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)

    total =0
    while len(truck_weights):
        time += 1
        total -= bridge.popleft()
        if total+truck_weights[0] <= weight:
            total += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    time += bridge_length

    return time

print(solution(2, 10, [7,4,5,6]))

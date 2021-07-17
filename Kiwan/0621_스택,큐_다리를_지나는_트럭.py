## 다리를 지나는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    total_weight = 0
    idx = 0
    N = len(truck_weights)

    now = 1
    q.append([now, truck_weights[idx]])
    total_weight += truck_weights[idx]
    idx += 1
    while True:
        now += 1
        if q:
            in_time, truck_weight = q.popleft()
            total_weight -= truck_weight
            if now - in_time < bridge_length:
                q.appendleft([in_time, truck_weight])
                total_weight += truck_weight
            if idx < N and total_weight + truck_weights[idx] <= weight:
                q.append([now, truck_weights[idx]])
                total_weight += truck_weights[idx]
                idx += 1
        else:
            break
    answer = now - 1
    return answer

#print(solution(2,10,[7,4,5,6]))
#print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))

# 0
# 1 10
# 2 10
# 3 10
# 4 10
# 5 10
# 6 10
# 7 10
# 8 10
# 9 10
# 10 10
# ...
# 100 10
# 101 없음
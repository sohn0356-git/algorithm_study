from heapq import *

def solution(scoville, K):
    answer = -1
    temp = 0
    # print(scoville)
    heapify(scoville)
    while scoville:
        a = heappop(scoville)
        if a >= K:
            answer = temp
            break
        else:
            if scoville != []:
                a += heappop(scoville)*2
                heappush(scoville, a)
                temp += 1
                # print(scoville, temp)

    return answer


# scoville = [1, 2, 3, 9, 10, 12]
# scoville = [1,1,1,1,1,1]
# scoville = [0,0,0,0,0]
# K = 7
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
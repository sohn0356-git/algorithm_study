# def solution(priorities, location):
#     answer = 0
#     answerList = []
#     maxIndex = priorities.index(max(priorities))
#     cnt = 0
#     rindex = 0
#     for i in range(len(priorities)):
#         cnt += 1
#         if maxIndex+i <= (len(priorities)-1):
#             priorities[maxIndex+i] = cnt
#         else:
#             priorities[rindex] = cnt
#             rindex +=1
#     answer = priorities[location]
#     return answer


#que를 사용한 풀이법!
#가중치와 idx를 넣어서 현재 뽑은 가중치가 최대이면 정답+1씩 증가
#location과 동일할시 break하고 탈출하여 정답 리턴
#중요포인트는 que에 원소가 하나 남았을 시 무한루프!
#탈출해주기 위해 que에 남은 원소가 있느냐를 같이 조건에 넣어줘야함
#max(que) 시에 que에 아무것도 없기때문에 error 뜸
from collections import deque
def solution(priorities, location):
    document= []
    answer = 0
    que = deque()
    for idx,importance in enumerate(priorities):
        que.append([importance,idx])
    while que:
        nowPrint = que.popleft()
        if que and nowPrint[0] < max(que)[0]:
            que.append(nowPrint)
        else:
            answer += 1
            if location == nowPrint[1]:
                break
    return answer
priorities = [2]
location = 0
solution(priorities, location)
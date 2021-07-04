from heapq import *

def solution(jobs):
    answer = 0
    before = -1 #작업하기 전 시간
    after = 0 # 작업완료시간
    cnt = 0 # 작업완료한 갯수
    task = [] #작업대기리스트
    while cnt < len(jobs): #작업이 다 끝나지 않았다면
        for job in jobs: 
            if before < job[0] <= after: #작업이 끝나기전에 요청이 들어오면 리스트에 넣기
                #작업시간, 작업요청시간 순으로 넣기
                heappush(task,[job[1],job[0]])
        #작업대기리스트에 작업이 있다면
        if task:
            cur = heappop(task)
            before = after #작업시작전 시간을 이전 작업완료시간으로 변경
            after += cur[0] #작업시간 더하기
            answer += after-cur[1] #정답에 요청시간으로부터 끝난시간까지 걸린시간 더하기
            cnt += 1
        else:
            #작업대기리스트에 아무것도 없으면 시간 흐름
            after += 1
    
    return answer//len(jobs) #평균시간이므로 작업갯수로 나누기


#heapq를 사용하지 않은 풀이

# def solution(jobs):
#     answer = 0
#     start = 0  # 현재까지 진행된 작업 시간
#     length = len(jobs)

#     jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

#     while len(jobs) != 0:
#         for i in range(len(jobs)):
#             if jobs[i][0] <= start:
#                 start += jobs[i][1]
#                 answer += start - jobs[i][0]
#                 jobs.pop(i)
#                 break
#             # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
#             if i == len(jobs) - 1:
#                 start += 1

#     return answer // length
from heapq import *

def solution(jobs):
    answer = 0
    before = -1
    after = 0
    cnt = 0
    task = []
    while cnt < len(jobs):
        for job in jobs:
            if before < job[0] <= after:
                #현재 작업중신것의 끝나는시간 after 에서 요청대기로 올릴때 기다려야할 시간을 미리 answer에 추가
                answer += after - job[0]
                heappush(task,job[1])
        
        
        if task:
            # task[0]은 현재 작업중인 소요시간, len(task)는 요청대기중이므로 길이*1초를 answer에 추가
            answer += task[0] + len(task)
            now = heappop(task)
            before = after
            after += now
            cnt += 1
        else:
            #시간이 흐름
            after += 1
    
    return answer

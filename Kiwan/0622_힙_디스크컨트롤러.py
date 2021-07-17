from heapq import *
from collections import deque
def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort()
    # jobs를 q로 만들어준다
    q = deque(jobs)
    
    # 현재 시간
    now = 0
    # 작업 시작 시간
    task_start = 0
    # 현재 시간에서 작업가능한 task를 담을 heap
    task_heap = []
    # 현재 작업중인 task
    working = []
    heapify(task_heap)
    while True:
        if working == []:
            try:
                in_time, task = q.popleft()
                while in_time <= now:
                    heappush(task_heap,[task, in_time])
                    in_time, task = q.popleft()
                q.appendleft([in_time, task])
                working.append(heappop(task_heap))
                task_start = now
            except:
                pass
        else:
            if task_start + working[0][0] <= now:
                task, in_time = working.pop()
                answer += now - in_time
                #task_time = now
                try:
                    in_time, task = q.popleft()
                    while in_time <= now:
                        heappush(task_heap,[task, in_time])
                        in_time, task = q.popleft()
                    q.appendleft([in_time, task])
                    working.append(heappop(task_heap))
                    task_start = now
                except:
                    pass

        if not q:
            break
        now += 1

    while task_heap:
        task, in_time = heappop(task_heap)
        now += task
        answer += now - in_time

    answer //= N
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]), 15)
print(solution([[0,5],[10,10],[11,5],[12,5],[13,5],[14,4],[15,6]]), 17)
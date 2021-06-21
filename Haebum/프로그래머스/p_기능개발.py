import math

def solution(progresses, speeds):
    answer = []
    complete = []
    for i in range(len(progresses)):
        #a = math.ceil((100 - progresses[i])/speeds[i])
        a = -((progresses[i]-100)//speeds[i])
        print(a)
        complete.append(a)
    

    temp = complete[0]
    cnt = 1
    for j in range(1,len(complete)):
        if complete[j] <= temp:
            cnt+=1
        else:
            temp = complete[j]
            answer.append(cnt)
            cnt = 1

        if j == len(complete)-1:
            answer.append(cnt)
    print(answer)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

solution(progresses, speeds)
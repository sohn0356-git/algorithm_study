def solution(priorities, location):
    answer = 0
    answerList = []
    maxIndex = priorities.index(max(priorities))
    cnt = 0
    rindex = 0
    for i in range(len(priorities)):
        cnt += 1
        if maxIndex+i <= (len(priorities)-1):
            priorities[maxIndex+i] = cnt
        else:
            priorities[rindex] = cnt
            rindex +=1
    answer = priorities[location]
    return answer

priorities = [2, 3, 9, 1, 1, 1]
location = 1
solution(priorities, location)
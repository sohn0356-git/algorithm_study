def solution(participant, completion):
    answer = ''
    answerList = {}
    for key in completion:
        if key in answerList:
            answerList[key] +=1
        else:
            answerList[key] = 1
    for i in participant:
        if i in answerList and answerList[i] >0:
            answerList[i] -=1
        else:
            answer = i
            break
    print(answer)
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

solution(participant, completion)
def solution(participant, completion):
    answer = ''
    answerList = {}
    for key in completion: #for문을 돌며
        if key in answerList: #정답 해시에 있을 경우
            answerList[key] +=1 # 벨류 +1 증가
        else: #없으면
            answerList[key] = 1 #해시 생성
    for i in participant: #도착자 체크
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
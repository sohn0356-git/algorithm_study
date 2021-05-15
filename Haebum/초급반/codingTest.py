def solution(t, r):
    answer = []
    # 1번 리프트번호가 동일할때
    # 티켓등급에 따라
    # 둘다 동일하면 아이디 숫자에 따라 결정
    sortAnswer = []
    for i in range(len(t)):
        sortAnswer.append([i,t[i],r[i]])
    for x in range(len(sortAnswer)):
        sortAnswer = sorted(sortAnswer, key = lambda x : (x[1], x[2],x[0]))
        answer.append(sortAnswer[0][2])
        del sortAnswer[0]
        for x in range(len(sortAnswer)):
            print(type(sortAnswer[1]))
            sortAnswer[1] += 1
    return answer

t = [0,1,3,0]
r = [0,1,2,3]

solution(t,r)
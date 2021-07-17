## 모의고사
def compare(p, answers):
    check = 0
    len_P = len(p)
    len_Answers = len(answers)
    if len_Answers >= len_P:
        for i in range(len_Answers):
            if p[i % len_P] == answers[i]:
                check += 1
    else:
        for i in range(len_Answers):
            if p[i] == answers[i % len_Answers]:
                check += 1
    return check

def solution(answers):
    answer = [0, 0, 0]
    answerd = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer[0] = compare(p1, answers)
    answer[1] = compare(p2, answers)
    answer[2] = compare(p3, answers)
    
    # for i in range(3):
    #     if answer[i] == 0:
    #         pass
    #     else:
    #         if answerd == []:
    #             answerd.append(i+1)
    #         else:
    #             for j in range(len(answerd)):
    #                 if answer[i] > answerd[j]:
    #                     if j == 0:
    #                         answerd.insert(0, i+1)
    #                     else:
    #                         answerd.insert(j-1, i+1)
    #                 else:
    #                     answerd.insert(j+1, i+1)
    for idx,value in enumerate(answer):
        if value == max(answer):
            answerd.append(idx+1)
             
        
    return answerd
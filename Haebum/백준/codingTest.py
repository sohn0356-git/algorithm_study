def solution(answers):
    answer = []
    mathGiveUp1 = [1,2,3,4,5] * 2000
    mathGiveUp2 = [2,1,2,3,2,4,2,5] * 1300
    mathGiveUp3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    num1 = 0
    num2 = 0
    num3 = 0
    
    for i in len(answers):
        if answers[i] == mathGiveUp1[i]:
            num1 +=1
        if answers[i] == mathGiveUp2[i]:
            num2 +=1
        if answers[i] == mathGiveUp3[i]:
            num3 +=1
    
    print(max(num1,num2,num3))
        
    return answer

ed = [1,2,3,4,5]

solution(ed)
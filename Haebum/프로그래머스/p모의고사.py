def solution(answers):
    mathGiveUp1 = [1, 2, 3, 4, 5] * 2000
    mathGiveUp2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    mathGiveUp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    num1 = 0
    num2 = 0
    num3 = 0

    for i in range(0,len(answers)):
        if answers[i] == mathGiveUp1[i]:
            num1 += 1
        if answers[i] == mathGiveUp2[i]:
            num2 += 1
        if answers[i] == mathGiveUp3[i]:
            num3 += 1

    if num1 > num2 :
        if num1 > num3:
            answer= [1]
        elif num1 < num3:
            answer = [3]
        else:
            answer = [1,3]
    elif num1 < num2:
        if num2 > num3:
            answer = [2]
        elif num2 < num3:
            answer = [3]
        else:
            answer = [2, 3]
    else:
        if num1 > num3:
            answer = [1,2]
        elif num1 < num3:
            answer = [3]
        else:
            answer= [1,2,3]

    return answer
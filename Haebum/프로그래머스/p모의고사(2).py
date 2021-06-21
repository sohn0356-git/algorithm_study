def solution(answers):
    result = []
    mathGiveUp1 = [1, 2, 3, 4, 5]
    mathGiveUp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    mathGiveUp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0,0,0]

    for idx,value in enumerate(answers):
        if value == mathGiveUp1[idx%len(mathGiveUp1)]:
            score[0] += 1
        if value == mathGiveUp2[idx%len(mathGiveUp2)]:
            score[1] += 1
        if value == mathGiveUp3[idx%len(mathGiveUp3)]:
            score[2] += 1

    for idx2,value2 in enumerate(score):
        if value2 == max(score):
            result.append(idx2+1)


    return result
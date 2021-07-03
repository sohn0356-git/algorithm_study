#dp문제
#rgb거리와 유사
#한쪽으로 정하고 넘어가면 되는데 맨처음집에 의해 마지막집도 결정되니
#처음집을 훔쳤냐 안훔쳤냐로 나눠서 dp 돌리기
#[][] 1일경우 훔친거 0일경우 안훔친거 뒤의 []은 집
def solution(money):
    answer = 0
    homes = len(money)
    firstSteal = [[0]*(homes) for _ in range(2)]
    firstNot = [[0]*(homes) for _ in range(2)]
    firstSteal[1][0] = money[0]
    firstSteal[0][1] = money[0]
    firstNot[1][1] = money[1]
    for steal in range(2,homes):
        firstSteal[0][steal] = max(firstSteal[1][steal-1],firstSteal[0][steal-1])
        firstNot[0][steal] = max(firstNot[1][steal-1],firstNot[0][steal-1])
        firstSteal[1][steal] = firstSteal[0][steal-1] + money[steal]
        firstNot[1][steal] = firstNot[0][steal-1] + money[steal]
    #누적형태이므로 마지막이 정답
    #max(처음집 훔치기[마지막집 안훔침], 처음집 안훔침[마지막집 훔침],처음집 안훔침[마지막집 안훔침])
    answer = max(firstSteal[0][homes-1],firstNot[1][homes-1],firstNot[0][homes-1])
    print(answer)
    return answer

money = [1, 2, 3, 1]
money2 = [4,1,1,6]
solution(money)
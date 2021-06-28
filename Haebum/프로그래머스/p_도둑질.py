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
    
    answer = max(firstSteal[0][homes-1],firstNot[1][homes-1],firstNot[0][homes-1])
    print(answer)
    return answer

money = [1, 2, 3, 1]
money2 = [4,1,1,6]
solution(money)
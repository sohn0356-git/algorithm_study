## 가장 큰 수
def solution(numbers):
    answerList = []
    numbers = list(map(str, numbers))

    for i in range(len(numbers)):
        origin = numbers[i]
        j = 0
        while len(numbers[i]) < 4:
            numbers[i] += numbers[i][j]
            j = (j+1) % len(origin)

        answerList.append([int(numbers[i]), origin])

    # print(answerList)
    answerList = sorted(answerList, reverse=True)
    return "".join([item[1] for item in answerList])

print(solution([6,10,2]))
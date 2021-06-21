def solution(array, commands):
    answer = []
    
    for i in commands:
        front = i[0] -1
        behind = i[1]
        findNum = i[2]-1
        sliceArray = array[front:behind]
        sliceArray.sort()
        answerNum = sliceArray[findNum]
        answer.append(answerNum)
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array,commands)
from itertools import permutations
import math

def solution(numbers):
    answer = 0
    element = []
    case = []

    removeCase = []
    for i in numbers:
        element.append(i)

    for j in range(1,len(numbers)+1):
        case.append(set(map(''.join,permutations(element,j))))

    for a in case:
        for b in a:
            if int(b) == 0 or int(b) == 1:
                pass
            else:
                removeCase.append(int(b))
    
    removeCase = set(removeCase)
    
    for value in removeCase:
        check = 0
        for i in range(2, int(math.sqrt(value)) + 1):
            if value % i == 0:
                check = 1
        if check == 0:
            answer += 1
    
    return answer
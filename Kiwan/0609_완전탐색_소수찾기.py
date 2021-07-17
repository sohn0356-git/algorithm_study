## 소수찾기
import math

def isPrimeNum(num):
    if num == 1 or num == 0:
        return 0

    limit = round(math.sqrt(num))

    for value in range(2, limit+1):
        if num % value == 0:
            return 0

    return 1

def stringToInt(stage, numbers, M, used, visited, numSet):
    N = len(numbers)
    if stage >= M:
        num = ''
        for j in used:
            if j != 0:
                num += j
        numSet.add(int(num))
        return
    for i in range(N):
        if visited[i] == 0:
            used[stage] = numbers[i]
            visited[i] = 1
            stringToInt(stage+1, numbers, M, used, visited, numSet)
            visited[i] = 0
    
def solution(numbers):
    answer = 0
    numSet = set()

    for i in range(1, len(numbers) + 1):
        used = [0] * i
        visited = [0] * len(numbers)
        stringToInt(0, numbers, i, used, visited, numSet)

    numlist = sorted(list(numSet))
    for num in numlist:
        if isPrimeNum(num):
            answer += 1

    return answer
answer = 0
def solution(numbers, target):
    dfs(numbers,0,0,target)
    return answer


def dfs(numbers,count,present,target):
    global answer
    if count == len(numbers):
        if present == target:
            answer +=1
        return
    dfs(numbers,count+1,present+numbers[count],target)
    dfs(numbers,count+1,present-numbers[count],target)

# numbers = [1, 1, 1, 1, 1]
# target = 3
# solution(numbers,target)
# print(answer)
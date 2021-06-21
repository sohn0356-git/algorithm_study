## 타겟넘버
def dfs(lev, numbers, target, sum, chk):
    if lev == len(numbers):
        if sum == target:
            chk[0] += 1
        return
    dfs(lev+1, numbers, target, sum+numbers[lev], chk)
    dfs(lev+1, numbers, target, sum+numbers[lev]*(-1), chk)

def solution(numbers, target):
    answer = 0
    chk = [0]
    dfs(1, numbers, target, numbers[0], chk)
    dfs(1, numbers, target, numbers[0]*(-1), chk)

    answer = chk[0]

    return answer

print(solution([2,3,-5,-7,9],2))
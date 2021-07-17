def solution(money):
    answer = 0
    
    N = len(money)
    res = [0 for _ in range(N)]
    res[0] = money[0]
    res[1] = res[0]
    for i in range(2,N):
        res[i] = max(res[i-2]+money[i],res[i-1])
    if answer < res[N-2]:
        answer = res[N-2]

    res = [0 for _ in range(N)]
    res[0] = 0
    res[1] = money[1]
    for i in range(2,N):
        res[i] = max(res[i-2]+money[i],res[i-1])
    if answer < res[N-1]:
        answer = res[N-1]

    return answer


print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]))
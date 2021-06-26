def solution(triangle):
    answer = -1
    N = len(triangle)
    res = [[-1 for __ in range(_)] for _ in range(1,N+1)]

    def dp(N, res, triangle):
        if N == 1:
            if res[N-1][0] == -1:
                res[N-1][0] = triangle[N-1][0]
            return max(res[N-1])
            
        elif N == 2:
            if max(res[N-1]) == -1:
                res[N-1][0] = triangle[N-1][0] + res[N-2][0]
                res[N-1][1] = triangle[N-1][1] + res[N-2][0]
            return max(res[N-1])
        else:
            if max(res[N-1]) == -1:
                n = len(triangle[N-1])
                for i in range(1,n+1):
                    if i == 1:
                        res[N-1][i-1] = triangle[N-1][i-1] + res[N-2][i-1]
                    elif i == n:
                        res[N-1][i-1] = triangle[N-1][i-1] + res[N-2][i-2]
                    else:
                        res[N-1][i-1] = triangle[N-1][i-1] + max(res[N-2][i-2], res[N-2][i-1])
            return max(res[N-1])

    for i in range(1,N+1):
        temp = dp(i, res, triangle)
        if answer < temp:
            answer = temp
    
    # dp(1,res,triangle)
    # for i in range(N):
    #     print(res[i])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
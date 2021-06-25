def solution(triangle):
    answer = 0
    lenth = len(triangle)
    dp = [[0] * lenth for _ in range(lenth)]
    

    for idx,i in enumerate(triangle):
        if idx == 0:
            dp[0][0] = i[0]
        for j in range(0,idx+1):
            if j == 0:
                dp[idx][j] = dp[idx-1][j] + i[j]
            elif j == idx:
                dp[idx][j] = dp[idx-1][j-1] + i[j]
            else:
                dp[idx][j] = max(dp[idx-1][j],dp[idx-1][j-1]) + i[j]
        if idx == lenth-1:
            answer = max(dp[idx])
    print(answer)
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
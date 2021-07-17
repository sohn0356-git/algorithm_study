# dp 풀이

def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    num = 1000000007
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles: #해당 좌표 웅덩이시 처리
                pass
            elif i==1 and j==1: #초기값 패스
                pass
            else: #그외 좌표
                if j-1 < 1:
                    dp[i][j] = dp[i-1][j]%num
                elif i-1 < 1:
                    dp[i][j] = dp[i][j-1] %num
                else:
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j])%num
    answer = dp[n][m]%num
    print(answer)
    return answer

m = 4
n = 3
puddles = [[2, 2]]
solution(m, n, puddles)
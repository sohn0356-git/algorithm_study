DP = [[0]*501 for _ in range(501)]
T = int(input())
for t in range(T):
    N = int(input())
    books = list(map(int,input().split()))
    sum_list = [0]*501
    for i in range(1,N+1):
        sum_list[i] = sum_list[i-1]+books[i-1]
    for i in range(501):
        for j in range(501):
            DP[i][j] = 0
    for i in range(1, N):
        for j in range(1, N-i+1):
            DP[j][i+j] = 987654321
            for k in range(j,i+j):
                DP[j][i+j]=min(DP[j][i+j],DP[j][k]+DP[k+1][i+j]+sum_list[j+i]-sum_list[j-1])

    print(DP[1][N])

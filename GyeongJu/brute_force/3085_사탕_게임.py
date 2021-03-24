N = int(input())
str = [list(input()) for _ in range(N)]

dirR = [1,0,-1,0]
dirC = [0,1,0,-1]
answer = 0

def calc():
    global answer, dirR, dirC, str, N
    for i in range(N):
        cnt = 1
        maxCnt = 1
        for j in range(N-1):
            if str[i][j] == str[i][j+1]:
                cnt += 1
            else:
                maxCnt = max(maxCnt, cnt)
                cnt = 1
        answer = max(answer, maxCnt, cnt)
    
    for i in range(N):
        cnt = 1
        maxCnt = 1
        for j in range(N-1):
            if str[j][i] == str[j+1][i]:
                cnt += 1
            else:
                maxCnt = max(maxCnt, cnt)
                cnt = 1
        answer = max(answer, maxCnt, cnt)

for i in range(N):
    for j in range(N):
        for d in range(4):
            nI = i + dirR[d]
            nJ = j + dirC[d]
            if nI>=0 and nI<N and nJ>=0 and nJ<N:
                if str[i][j] != str[nI][nJ]:
                    str[i][j], str[nI][nJ] = str[nI][nJ], str[i][j]
                    calc()
                    str[i][j], str[nI][nJ] = str[nI][nJ], str[i][j]
print(answer)

            
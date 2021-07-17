def solution(N, number):
    if N == number:
        return 1
    answer = -1
    flag = 0
    dp = [0]*9
    dp[1] = [[N]]
    for i in range(2,9):
        dp[i],flag = DP(dp[i-1],number,N)
        if flag == 1:
            answer = i
            break
    return answer

def DP(dpList,number,N):
    temp = []
    flag = 0
    for i in dpList:
        if flag == 1:
            break
        for j in i:
            nn = int(str(j)+str(N))
            plus = j + N
            minus = j - N
            multi = j * N
            division = j // N
            calList = [nn,plus,minus,multi,division]
            if number in calList:
                flag = 1
                break
            else:
                flag = 0
            temp.append(calList)
    return temp,flag


N = 2
number = 11
solution(N, number)
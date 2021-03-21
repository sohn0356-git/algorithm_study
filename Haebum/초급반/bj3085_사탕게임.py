import copy
#정답의 최대는 50

#shallow copy deep copy (정리하기!!)

#n*n의 그래프에서 서로 다른 사탕을 한번 바꿀 수 있다
#그때 같은 사탕으로 이루어진 가장 긴 줄(행 또는 열)을 골라
#같은 사탕의 갯수를 출력

#행 방향으로 한번 바꿔서 해보고 열방향으로도 한번 바꿔서 해볼 계획
#브루트포스로 전부 해봐서 가장 큰 수를 정답에 저장하여 출력
#가로방향,세로방향 사탕 바꾸기 후
#연속된 같은 사탕 갯수 세기

#최대값 최소값 얼마정도인지
#시간복잡도는 50**4 5**4 * 10 **4 가능
#공간복잡도는 파악... n이 50까지가능 char이므로 1byte 50*50 = 2500byte = 2.5kb

def changeGraph(graph):
    for i in range(n-1):
        for j in range(n):
            if graph[i][j] != graph[i+1][j]:
                graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
                answerCheck(graph)
                graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]

            if graph[j][i] != graph[j][i+1]:
                graph[j][i], graph[j][i+1] = graph[j][i+1], graph[j][i]
                answerCheck(graph)
                graph[j][i], graph[j][i+1] = graph[j][i+1], graph[j][i]

def answerCheck(sugar):
    global answer
    for k in range(n):
        witdhCnt=1
        heightCnt=1
        for l in range(n-1):
            if sugar[l][k] == sugar[l+1][k]:
                heightCnt += 1
            else:
                if answer < heightCnt:
                    answer = heightCnt
                heightCnt = 1
            if sugar[k][l] == sugar[k][l+1]:
                witdhCnt += 1
            else:
                if answer < witdhCnt:
                    answer = witdhCnt
                witdhCnt = 1 
        if answer < heightCnt:
            answer = heightCnt
        if answer < witdhCnt:
            answer = witdhCnt

n = int(input())
graph = []
answer= 0
for i in range(n):
    graph.append(list(input()))

changeGraph(graph)
print(answer)

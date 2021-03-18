import copy
#정답의 최대는 50

#shallow copy deep copy

#n*n의 그래프에서 서로 다른 사탕을 한번 바꿀 수 있다
#그때 같은 사탕으로 이루어진 가장 긴 줄(행 또는 열)을 골라
#같은 사탕의 갯수를 출력

#행 방향으로 한번 바꿔서 해보고 열방향으로도 한번 바꿔서 해볼 계획
#브루트포스로 전부 해봐서 가장 큰 수를 정답에 저장하여 출력
#가로방향,세로방향 사탕 바꾸기 후
#연속된 같은 사탕 갯수 세기

#시간복잡도는 50**4 5**4 * 10 **4 가능
#공간복잡도는 

def changeGraph(graph):
    answerCheck(graph)
    for i in range(n):
        for j in range(n):
            if i==n-1:
                continue
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
        for l in range(n):
            if l==n-1:
                continue
            if sugar[l][k] == sugar[l+1][k]:
                heightCnt += 1
            if sugar[k][l] == sugar[k][l+1]:
                witdhCnt += 1
        if answer < witdhCnt:
            answer = witdhCnt
        if answer < heightCnt:
            answer = heightCnt

n = int(input())
graph = []
answer= 0
for i in range(n):
    graph.append(list(input()))

changeGraph(graph)
print(answer)

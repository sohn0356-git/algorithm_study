# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# BFS : 큐
# DFS : 재귀
from collections import deque
def dfs(dep, arr, tickets, visited, course, answerList):
    if sum(visited) == len(tickets):
        temp = course.copy()
        temp.extend([arr])
        answerList.append(temp)
        return
    for i, next in enumerate(tickets):
        if visited[i] != 1 and arr == next[0]:
            visited[i] = 1
            course.append(next[0])
            dfs(next[0], next[1], tickets, visited, course, answerList)
            visited[i] = 0
            course.pop()

def solution(tickets):
    answer = []
    n = len(tickets)
    tickets.sort(key = lambda x : x[0], reverse = True)
    
    answerList = []
    for i in range(n):
        visited = [0] * n
        course = []
        if tickets[i][0] == "ICN":
            visited[i] = 1
            course.append(tickets[i][0])
            dfs(tickets[i][0], tickets[i][1], tickets, visited, course, answerList)

    print(answerList)
    
    while answerList:
        if answer == []:
            answer = answerList.pop()
        else:
            if answerList[-1] < answer:
                answer = answerList.pop()
            else:
                answerList.pop()

    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))


# def solution(n, costs):
#     answer = 0

#     costs.sort(key=lambda x:(x[0],x[1]))
#     visited = [0] * n
#     answerList = []

#     cnt = 0
#     for i, elem in enumerate(costs):
#         island1, island2, cost = elem
#         if i == 0:
#             visited[island1] = 1
#             visited[island2] = 1
#             cnt += 2
#             answerList.append([i,island1,island2,cost])
#         else:
#             if visited[island1] == 0 and visited[island2] == 0:
#                 visited[island1] = 1
#                 visited[island2] = 1
#                 cnt += 2
#                 answerList.append([i,island1,island2,cost])
#             elif visited[island1] == 1 and visited[island2] == 0:
#                 visited[island2] = 1
#                 cnt += 1
#                 answerList.append([i,island1,island2,cost])
#             else:
#                 # visited[island1] == 0 and visited[island2] == 1
#                 # visited[island1] == 1 and visited[island2] == 1
#                 for j, a_elem in enumerate(answerList):
#                     a_i, a_island1, a_island2, a_cost = a_elem
#                     if island2 == a_island2 and cost < a_cost:
#                         if visited[island1] == 0:
#                             visited[island1] = 1
#                         cnt += 1
#                         answerList[j] = [i, island1, island2, cost]
        
#     print(answerList)
#     answer = sum(list(map(lambda x: x[3], answerList)))
#     return answer

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x : (x[2], x[0]))
    print(costs)
    unions = []
    edge = 0
    for i, item in enumerate(costs):
        v1, v2, cost = item
        temp = [None, None]
        if unions == []:
            unions.append({v1:1, v2:1})
            answer += cost
            edge += 1
        else:
            if edge >= n-1:
                break
            for idx1, union1 in enumerate(unions):
                if union1.get(v1):
                    temp[0] = idx1
            for idx2, union2 in enumerate(unions):
                if union2.get(v2):
                    temp[1] = idx2
            if temp[0] != None and temp[1] != None:
                if temp[0] != temp[1]:
                    unions[temp[0]].update(unions[temp[1]])
                    unions.pop(temp[1])
                    answer += cost
                    edge += 1
                else:
                    pass
            elif temp[0] != None and temp[1] == None:
                unions[temp[0]][v2] = 1
                answer += cost
                edge += 1
            elif temp[0] == None and temp[1] != None:
                unions[temp[1]][v1] = 1
                answer += cost
                edge += 1
            else:
                unions.append({v1:1, v2:1})
                answer += cost
                edge += 1

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]), 4)
print(solution(4, [[0,1,1],[0,2,8],[1,2,5],[1,3,1],[2,3,8]]), 7)
print(solution(4, [[0,1,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1]]), 3)
print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]), 15)
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]), 7)


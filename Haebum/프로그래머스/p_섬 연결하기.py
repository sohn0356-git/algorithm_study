def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n+1)]
    

    # 부모 노드 찾기
    def find(cost):
        if cost == parent[cost]:
            return cost
        else:
            parent[cost] = find(parent[cost])
            return parent[cost]

    # 부모노드 통일하기
    def union(x,y):
        x = find(x)
        y = find(y)
        if x!=y:
            parent[y] = x

    for cList in costs:
        startIsland = cList[0]
        endIsland = cList[1]
        cost = cList[2]
        if find(startIsland) != find(endIsland):
            union(startIsland,endIsland)
            answer += cost
    print(answer)
    return answer

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4
solution(n, costs)
def Find(x, parent):
    if x == parent[x]:
        return x
    else :
        parent[x] = Find(parent[x], parent)
        return parent[x]

# y부모 - x자식 관계 만들어주는 함수
def Union(x, y, parent, answer, edge, cost):
    # 루트를 찾는다.
    x = Find(x, parent)
    y = Find(y, parent)

    # 루트가 같다면 같은 트리이므로 합칠 필요가 없음
    if x==y:
        return

    # x의 루트를 y로 바꿈
    parent[x] = y
    # answer에 비용 추가, 간선 1 증가
    answer[0] += cost
    edge[0] += 1

def solution(n, costs):
    answer = [0]
    costs.sort(key=lambda x : (x[2], x[0]))
    print(costs)
    parent = [i for i in range(n)]
    edge = [0]
    print(parent)

    for i, item in enumerate(costs):
        if edge[0] >= n-1:
            break;
        v1, v2, cost = item
        Union(v2, v1, parent, answer, edge, cost)

    return answer[0]

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]), 4)
print(solution(4, [[0,1,1],[0,2,8],[1,2,5],[1,3,1],[2,3,8]]), 7)
print(solution(4, [[0,1,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1]]), 3)
print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]), 15)
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]), 7)
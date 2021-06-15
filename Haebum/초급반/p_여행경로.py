# dfs 풀 예정
# 방문 시 visited에 표시
# icn끼리 정렬하여 첫번째걸 넣고 가기
# 두번째 원소를 불러오소 원소에 해당하는것들을 찾고 그중 가장 빠른것을 방문
# 공항갯수 10000 -> 10^4

def solution(tickets):
    routes = dict()
    tickets.sort(reverse=True)
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    return ans


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)
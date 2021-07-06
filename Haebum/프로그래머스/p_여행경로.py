# 스택과 해시를 사용한 풀이
# 공항갯수 10000 -> 10^4

def solution(tickets):
    routes = dict()
    tickets.sort(reverse=True)
    for t1, t2 in tickets: #두개의 원소를 뽑음
        if t1 in routes: #키값이 루트안에 있다면
            routes[t1].append(t2) #벨류값 추가
        else: #없으면 해시 키:[벨류] 생성
            routes[t1] = [t2]
    st = ['ICN'] #초기값
    ans = []
    while st:
        top = st[-1] #스택에 마지막값
        if top not in routes or len(routes[top])==0: #해시에 없거나 키에 해당하는 벨류가 0일경우
            ans.append(st.pop()) #정답에 마지막 스택 값 넣기
        else: #해시 존재하면서 벨류가 있을경우
            st.append(routes[top].pop()) #키에 해당하는 벨류를 빼서 스택에 추가
    ans.reverse() #역순으로 정렬
    return ans


tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
solution(tickets)
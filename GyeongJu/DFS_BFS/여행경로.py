def dfs(answer, visited, tickets):
    if len(answer)==len(tickets)+1:
        return answer
    for idx, ticket in enumerate(tickets):
        if not visited[idx] and answer[-1]==ticket[0]:
            visited[idx]=True
            answer.append(ticket[1])
            dfs(answer, visited, tickets)
            if len(answer)==len(tickets)+1:
                return answer
            answer.pop()
            visited[idx]=False

def solution(tickets):
    answer = []
    visited = [False]*len(tickets)
    tickets=sorted(tickets, key=lambda tickets: tickets[1])
    
    answer.append("ICN")
    dfs(answer, visited, tickets)
    return answer

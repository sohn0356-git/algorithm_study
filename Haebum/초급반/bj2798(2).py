n,m = map(int,input().split())

answer = 0
card = list(map(int,input().split())) 
used = [0]*3
visited = [0]*(n+1)

def solve(stage):
    global answer
    if stage==3:
        sum = 0
        for i in used:
            sum += card[i]
        if sum <= m:
            if answer < sum:
                answer = sum
        return
        
    for i in range(n):
        if visited[i] == 0:
            if stage> 0:
                if used[stage-1] >= i:
                    continue
            visited[i] = 1
            used[stage] = i
            solve(stage+1)
            visited[i] = 0

solve(0)
print(answer)

    
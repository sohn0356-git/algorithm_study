n, m = map(int,input().split())

used = [0]*m 
visited = [0]*(n)
card = list(map(int,input().split()))
card.sort()

def solve(stage):
    if stage==m:
        for i in used:
            print(card[i],end=' ')
        print()
        return
    for i in range(n):
        if visited[i] ==0:
            if stage>0 and used[stage-1]> i: #오름차순 정렬
                continue
            if i>0:
                if visited[i-1] == 0 and card[i-1] == card[i]:
                    continue
            visited[i] = 1
            used[stage] = i
            solve(stage+1)
            visited[i] = 0

solve(0)


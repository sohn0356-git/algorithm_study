n,m = map(int,input().split())
answer = 0 #정답출력
card = list(map(int,input().split()))  #카드 리스트 5 6 7 8 9  n=5 카드덱의 카드갯수? m=21 목표치
used = [0]*3 #몇번째 카드를 뽑았는지 담기(3개의 카드) [0,0,0]
visited = [0]*(n+1) #사용한 카드는 중복안되게 [0,0,0....n+1개의 0]

#재귀함수(조합론)
def solve(stage):
    global answer
    if stage==3: #k장의 카드를 다 뽑으면
        sum = 0 #세장의 합계를 담기위한 변수
        for i in used: #카드를 돌면서
            sum += card[i] #합계
        if sum <= m: #합계가 지정한 목표치보다 적을때
            if answer < sum: #현재 정답이 합계보다 작을때
                answer = sum #현재 정답을 합계로 저장
        return
        
    for i in range(n):
        if visited[i] == 0: #중복제외
            if stage> 0: #오름차순 정렬
                if used[stage-1] >= i: 
                    continue
            visited[i] = 1 #중복제외를 위해 넣어둠(0,1,2,3,4 중 사용한카드는 1로지정)
            used[stage] = i #고른 카드 리스트에 담기
            solve(stage+1) #다음 카드 고르러 가기
            visited[i] = 0

solve(0) 
print(answer)

##시간복잡도 nP3(n*n-1*n-2) -> nc3(n*n-1*n-2/3*2*1)
    
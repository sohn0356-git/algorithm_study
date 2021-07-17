#1~n자연수 중 m개를 고른 수열 출력
n,m = map(int,input().split())
card = [] #1~n자연수 리스트

used= [0]*m #뽑은 자연수 자리번호
visited = [0]*(n) #사용한 자연수

for i in range(1,n+1): #자연수 리스트에 담기
    card.append(i)

def solve(stage):
    if stage==m: #다 뽑았을때 출력
        for i in used:
            print(card[i],end=" ")
        print()
        return

    for i in range(n):
        if visited[i] ==0: #사용하지 않은 자연수일때
            if stage>0 and used[stage-1]> i: #오름차순 정렬
                continue
            visited[i] =1 #사용한 자연수로 체크
            used[stage] = i #뽑은 자연수자리수 리스트에 넣기
            solve(stage+1) #다음 자연수 뽑으러 가기
            visited[i] = 0 #사용한 자연수는 다시 안한걸로 반환

solve(0)
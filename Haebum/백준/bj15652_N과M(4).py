#1~n자연수 중 m개를 고른 수열 출력
n,m = map(int,input().split())
card = [] #1~n자연수 리스트

used= [0]*m #뽑은 자연수 자리번호

for i in range(1,n+1): #자연수 리스트에 담기
    card.append(i)

def solve(stage):
    if stage==m: #다 뽑았을때 출력
        for i in used:
            print(card[i],end=" ")
        print()
        return

    for i in range(n):
        if stage>0 and used[stage-1] >i:
            continue
        used[stage] = i #뽑은 자연수자리수 리스트에 넣기
        solve(stage+1) #다음 자연수 뽑으러 가기

solve(0)
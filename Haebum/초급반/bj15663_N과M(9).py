#1~n자연수 중 m개를 고른 수열 출력
n,m = map(int,input().split())
card = list(map(int,input().split())) #1~n자연수 리스트
card.sort() #오름차순 정렬

used= [0]*m #뽑은 자연수 자리번호
visited = [0]*(n) #사용한 자연수
usedlist = []
usedmap = {}

#딕셔너리는 해시테이블 구조를 가짐(시간복잡도o(1))
def solve(stage):
    if stage==m: #다 뽑았을때 출력
        if usedmap.get(tuple(used)):
            return
        else:
            new_used = []
            for i in used:
                new_used.append(i)
            usedlist.append(new_used)
            usedmap[tuple(new_used)] = 1
            for i in new_used:
                print(i,end=" ")
            print()
        return

    for i in range(n):
        if visited[i] ==0: #사용하지 않은 자연수일때
            visited[i] =1 #사용한 자연수로 체크
            used[stage] = card[i] #뽑은 자연수자리수 리스트에 넣기
            solve(stage+1) #다음 자연수 뽑으러 가기
            visited[i] = 0 #사용한 자연수는 다시 안한걸로 반환

solve(0)
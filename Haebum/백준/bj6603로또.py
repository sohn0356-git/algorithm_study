#로또 1~49중에서 k개의 숫자를 뽑고
#그 k개의 숫자들 중 6개를 뽑아 경우의수 출력

#여러개의 테스트 케이스가 주어짐
#ex) 로또중 8개로 이루어진
# 1,2,3,4,5,6,7,8 중에서 6개를 뽑아 경우의수찾기
# 마지막 입력란엔 0

# 7 1 2 3 4 5 6 7  7=k개 1~7은 s =k개의 원소
# 8 1 2 3 5 8 13 21 34
# 0

s= [] #테스트케이스 리스트
k = 1  #테스트케이스의 원소값 및 입력탈출
while(k!=0): #0 입력전까지 반복
    inputdata = list(map(int,input().split())) #입력값을 리스트화
    k = inputdata[0] #첫번째 입력값은 원소의개수를 의미(마지막 0 입력시 while 탈출!)
    inputdata.remove(k) #첫번째 입력값 리스트에서 제거
    s.append(inputdata) #s리스트에 담음


used = [0]*6 #고른 숫자를 담을 리스트
visited = [0]*50 #사용한 숫자를 담을 리스트(중복제거용)


def solve(stage,num): #stage는 숫자위치,num은 테스트케이스번호
    if stage ==6: #6개의 숫자를 다 골랐을때
        for i in used: #고른 숫자들을 출력
            print(i,end=" ")
        print()
        return
    else: #아직 6개의 숫자를 다 고르지 못했을때
        for i in s[num]: #첫번째케이스의 숫자 하나씩 꺼내기
            if stage>0: #오름차순 정렬
                if used[stage-1] >=i:
                    continue
            if visited[i]==0: #사용안한 숫자일경우
                visited[i] =1 #사용한 숫자로 변경
                used[stage] = i #고른 숫자 리스트에 담기
                solve(stage+1,num) #다음 숫자 고르러가기
                visited[i] =0 #다시 초기화

for i in range(len(s)): #테스트케이스별 출력
    solve(0,i)
    print() #테스트 케이스 사이엔 빈줄 출력
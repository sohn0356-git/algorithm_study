#

import sys

# n = 접시의 수, d = 초밥의 가짓수
# k = 연속해서 먹는 수, c = 쿠폰 번호

# 2<= n <= 30,000  2<= d <= 3000
# 2<= k <= 3,000 1<= c <= d

n, d, k, c = map(int,sys.stdin.readline().split())

chobabs = []

#초밥 벨트
for i in range(n):
    chobab = int(sys.stdin.readline())
    chobabs.append(chobab)

#정답
answer = 0

#중복제거 셋
checkSet = set()

#start i
for i in range(n):
    if answer == k+1:
        break
    #end j 먹은개수만큼 돌기
    for j in range(i,i+k):
        if j > n-1:
            j = j%n
        checkSet.add(chobabs[j])
    checkSet.add(c)
    answer = max(answer,len(checkSet))
    checkSet.clear()

print(answer)

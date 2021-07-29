import sys

# n = 용액의 수 2<= n <= 100,000
n = int(sys.stdin.readline())

# 용액 특성
nlist = list(map(int,sys.stdin.readline().split()))

#정렬
nlist.sort()

#두 용액
minNum = 0 
maxNum = n-1

#정답찾기
def twoPoint(left,right,check):
    global minNum, maxNum
    # 둘이 바뀌기 전까지
    while left < right:
        # 두 용액의 합
        sumNum = nlist[left] + nlist[right]
        # 두 용액의 합이 기준보다 적을때
        if abs(sumNum) < check:
            #기준을 변경
            check = abs(sumNum)
            #정답 저장
            minNum = left
            maxNum = right
        # 두 용액의 합이 양수일때
        if sumNum > 0:
            # 양의 최대값을 감소
            right -= 1
        # 두 용액의 합이 음수일때
        elif sumNum < 0:
            # 음의 최대값을 감소
            left +=1
        # 0이면 탈출
        else:
            break

# 인덱스기준: 음의 최대 0 양의 최대 n-1 기준치
twoPoint(0,n-1,sys.maxsize)
print(nlist[minNum],nlist[maxNum])

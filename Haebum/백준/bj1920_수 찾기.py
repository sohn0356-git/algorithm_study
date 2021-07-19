import sys

n = int(sys.stdin.readline())
nList = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))

#데이터값은 정렬 필수
nList.sort()

# target이랑 nList를 넘겨주면 이분탐색으로 해당 값 가져옴
def binary_target(target,nList):
    start = 0
    end = len(nList)-1

    while start <= end:
        mid = (start+end)//2
        if nList[mid] == target:
            return 1
        elif nList[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

for i in mList:
    answer = binary_target(i,nList)        
    print(answer)

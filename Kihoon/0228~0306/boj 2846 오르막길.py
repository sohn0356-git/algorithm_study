# N: 수열의 크기 (1 ≤ N ≤ 1000)
# Pi: N개의 양의 정수 (1 ≤ Pi ≤ 1000)가 주어진다. 각 숫자는 상근이가 측정한 높이이다.
# 가장 큰 오르막길

## 같은 높이가 연속될 때 오류남

N = int(input())
Pi = list(map(int,input().split(' ')))
temp = 0
tempheight = [];


for i in range(1,N): #12 20 1 3 4 4 11 1
    if Pi[i-1] < Pi[i]: #오르막길
        temp += Pi[i] - Pi[i - 1]
        if(i==N-1):
            tempheight.append(temp);
    else : #정점이라 판단되면 누적 높이를 높이배열에 넣기
        tempheight.append(temp)
        temp=0

print(tempheight)

if tempheight.count(0) == N-1:
    print(0)
else:
    print(max(tempheight))
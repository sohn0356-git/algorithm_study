# 현재 상태



# 다룰 수 있는 언어



* Python(3번까지는 풀었는데? 오?)
* 사실 알고리즘을 풀기보다는 다른 사람이 푸는걸 좀 보고싶다.



# 알고있는 알고리즘







# 초급반 문제



```python
# 11021

t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print("Case #{}: {}".format(i+1,a+b))

    
    
```



```python
# 1065

n = int(input())
hs = 0;
for i in range(1, n+1):
    if i <= 99:
        hs += 1

    else:
        ns = list(map(int,str(i)))
        if ns[0] - ns[1] == ns[1] - ns[2]:
            hs += 1

print(hs)

```



```python
# 1977

m = int(input())
n = int(input())
result = []
for i in range(1, 10001):
    sq = i * i
    if sq >= m and sq <= n:
        result.append(sq)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])
    
#조금 무식하게 풀은거 같긴 하지만 어쨌든 풀었습니다.
#근데 여기 찐 초급자 저 밖에 없는거 같은데 기분 탓인가요?
#ㄹㅇ 다들 못한다고 하셨는데 다 잘해서 상처받음 
```



```python
#2798

n, m = map(int,input().split())
alist = list(map(int,input().split()))
result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if alist[i] + alist[j] + alist[k] > m:
                continue
            else:
                result = max(result, alist[i] + alist[j] + alist[k])

print(result)
```


# 현재 상태



# 다룰 수 있는 언어



* Python(3번까지는 풀었는데? 오?)
* 사실 알고리즘을 풀기보다는 다른 사람이 푸는걸 좀 보고싶다.



# 알고있는 알고리즘







# 초급반 문제



```python
11021

t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print("Case #{}: {}".format(i+1,a+b))

    
    
```



```python
1065

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


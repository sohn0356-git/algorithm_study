n, m = map(int, input().split(' '))
list = list(map(int, input().split(' ')))
sum = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            temp = list[i] + list[j] + list[k]
            if temp > m:
                continue
            else:
                sum = max(sum, temp)
print(sum)
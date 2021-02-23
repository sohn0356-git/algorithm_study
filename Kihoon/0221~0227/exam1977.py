a = int(input());
b = int(input());
s=0;
number = [];

for i in range(1,10001):
    s = i * i
    if a <= s and s <= b :
        number.append(s)

if len(number)==0:
    print(-1)
else:
    print(sum(number))
    print(number[0]);





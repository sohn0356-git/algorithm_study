a = int(input());
b = int(input());
c = int(input());

result = a*b*c

myarr = []

while result !=0:
    t = result % 10
    myarr.append(t)
    result = int(result/10)

for i in range(10):
    print(myarr.count(i))






#M, N = input().split();
M = int(input());
N = int(input());

nlist = [];

for num in range(1, 101):
    pNum = num * num;
    if pNum in range(M, N+1):
        nlist.append(pNum);

if nlist == []:
    print(-1);
else:
    print(sum(nlist));
    print(nlist[0]);



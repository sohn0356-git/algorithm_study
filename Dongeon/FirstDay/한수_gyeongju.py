def hansu(n) :
    list1 = set();
    if n < 100:
        return 1;
    else :
        n = list(str(n));
        for i in range(0, len(n)-1) :
            differ = int(n[i]) - int(n[i+1])
            list1.add(differ);
            if len(list1)>1:
                return 0;
        return 1;

num = int(input());
sum = 0;
for i in range(1,num+1):
    if hansu(i) == 1 :
        sum += 1;
print(sum);
def hansu(n) :
    list1 = [];
    if n < 10 :
        return 1;
    else :
        n = list(str(n));
        for i in range(0, len(n)-1) :
            differ = int(n[i]) - int(n[i+1])
            list1.append(differ);
        list1 = set(list1);

        if len(list1) == 1 :
            return 1;
        else :
            return 0;

num = int(input());
sum = 0;
for i in range(1,num+1):
    if hansu(i) == 1 :
        sum +1;
print(sum);
import random

inputNum1, inputNum2 = map(int, input().split());
list1 = list(map(int, input().split()));

list1.sort(reverse=True);

list2 = [0];

for i in range(0,len(list1)) :
    for j in range(i+1, len(list1)) :
        for k in range(j+1, len(list1)) :
            if(list1[i] + list1[j] + list1[k] <= inputNum2) :
                list2.append(list1[i] + list1[j] + list1[k]);

list2.sort(reverse=True);

print(list2[0])






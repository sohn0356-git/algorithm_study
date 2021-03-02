
inputNum = int(input())

list1 = list(map(int, input().split()));
list2 = [0]
min = 0;
max = 0;

list1.append(0);

min = list1[0];
for i in range(0, len(list1)-1) :
    if (list1[i] < list1[i+1]) :
        max = list1[i+1];
    if(list1[i] >= list1[i+1]) :
        list2.append(max - min);
        max = 0;
        min = list1[i+1];

list2.sort(reverse = True);

print(list2[0]);




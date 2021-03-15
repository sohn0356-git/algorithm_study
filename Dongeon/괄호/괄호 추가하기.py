

equationSize = int(input());
equation = input()

#equationSize = 9;


#equation = "3+8*7-9*2"

equationSum = 0

equation2 = equation;
count = 0
while '+' in equation2 or '-' in equation2 or '*' in equation2 :
    count += 1;
    if equation2[count] == '+' or equation2[count] == '-' or equation2[count] == '*' :
        sample = str(eval(equation2[0:count+2]))
        equation2 = equation2.replace(equation2[0:count+2], sample)
        count = 0



list1= []
list1.append(int(equation2))

n = int(equationSize)
num = (n+1)//4; # 괄호의 개수



maxNum = 0;

for j in range(num+1) :
    used = [0] * j


    def solve(stage) :
        equation1 = equation


        if stage == j :
            for i in used :
                #print(i, end =" ")
                replace = str(eval(equation[i:i+3]))
                #equation1 = equation.replace('8*3', '24')
                equation1 = equation1.replace(equation[i:i+3], replace)
            #print()
            #print(equation1, end = " ")
            #print(eval(equation1))
            #print()
            list1.append(eval(equation1));
            return

        for i in range(0,n-2,2) :
            if stage > 0 and i <= used[stage-1]+2  :
                continue;
            used[stage] = i;
            solve(stage + 1)
    solve(0);


list1.sort(reverse=True)
print(list1[0])






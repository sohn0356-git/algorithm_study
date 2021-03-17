

equationSize = int(input());
equation = input()

#equationSize = 9;
#equation = "3+8*7-9*2"




equation = equation + 'A'


def equationSum(equation) :
    equation2 = equation;
    count1 = 0
    while '+' in equation2 or '-' in equation2 or '*' in equation2 :
        count1 += 1;
        if equation2[count1] == '+' or equation2[count1] == '-' or equation2[count1] == '*' :
            if equation2[count1+2].isdecimal() and  equation2[count1+2] != 'A':
                sample = str(eval(equation2[0:count1 + 3]))
                equation2 = equation2.replace(equation2[0:count1 + 3], sample)
                count1 = 0
            else :
                sample = str(eval(equation2[0:count1+2]))
                equation2 = equation2.replace(equation2[0:count1+2], sample)
                count1 = 0
    equation2 = equation2.replace('A',"")
    result = int(equation2)
    return result;



list1= []
list1.append(equationSum(equation))
#print(list1)

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
                if eval(equation[i:i+3]) < 0 :
                    continue;
                replace = str(eval(equation[i:i+3]))
                equation1 = equation1.replace(equation[i:i+3], replace)
            print()
            print(equation1, end = " ")
            print(equationSum(equation1))
            print()

            list1.append(equationSum(equation1));
            return

        for i in range(0,n-2,2) :
            if stage > 0 and i <= used[stage-1]+2  :
                continue;
            used[stage] = i;
            solve(stage + 1)
    solve(0);

#print(list1)
list1.sort(reverse=True)
print(list1[0])






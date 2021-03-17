from collections import deque

def solve(idx):
    global num, op, ans
    if idx>=len(op):
        
        op_cp = []
        num_cp = []
        for i in op:
            op_cp.append(i)
        for i in num:
            num_cp.append(i)
        i = -1
        while True:
            i += 1
            if i>=len(op_cp):
                break
            if op_cp[i]=='+' or op_cp[i]=='-' or op_cp[i]=='*':
                continue
            if op_cp[i]=='P':
                num_cp[i] += num_cp[i+1]
            elif op_cp[i]=='S':
                num_cp[i] -= num_cp[i+1]
            elif op_cp[i]=='M':
                num_cp[i] *= num_cp[i+1]
            num_cp.pop(i+1)
            op_cp.pop(i)
        for i in range(len(op_cp)):
            if op_cp[i]=='+':
                num_cp[i+1] = num_cp[i] + num_cp[i+1]
            elif op_cp[i]=='-':
                num_cp[i+1] = num_cp[i] - num_cp[i+1]
            elif op_cp[i]=='*':
                num_cp[i+1] = num_cp[i] * num_cp[i+1]
        if(ans<num_cp[-1]):
            ans = num_cp[-1]
        return
    t = op[idx]
    if op[idx]=='+':
        op[idx] = 'P'
    elif op[idx]=='-':
        op[idx] = 'S'
    elif op[idx]=='*':
        op[idx] = 'M'
    solve(idx+2)
    op[idx] = t
    solve(idx+1)

N = int(input())
str = input()

num = []
op = []
ans = -(1<<32)

for i in str:
    if i=='+' or i=='-' or i=='*':
        op.append(i)
    else:
        num.append(int(i))

solve(0)
print(ans)
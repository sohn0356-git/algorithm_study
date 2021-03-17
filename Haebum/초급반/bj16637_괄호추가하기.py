from collections import deque


n = int(input())
str = input()
visited = [0] * (n//2+1) # opr(연산자)에 따라 괄호를 했는지 안했는지 확인
answer = -2**31 #경주님은 -()
def calc(num1,opr,num2):
    if opr == "+":
        result = int(num1) + int(num2)
    elif opr == "-":
        result = int(num1) - int(num2)
    elif opr == "*":
        result = int(num1) * int(num2)
    return result

def answerCalc(visited):
    queue = deque()
    idx = 0
    for i in str:
        if i.isnumeric():
            if visited[idx] == 1:
                opr = queue.pop()
                a = queue.pop()
                result = calc(a,opr,i)
                queue.append(result)
            else:
                queue.append(int(i))
        else:
            idx +=1
            queue.append(i)
    while queue:
        try:
            a = queue.popleft()
            opr = queue.popleft()
            b = queue.popleft()
            result = calc(a,opr,b)
            queue.appendleft(result)
        except:
            return a

def solve(stage):
    global answer
    result = answerCalc(visited)
    if answer < result:
        answer = result
    for i in range(1,(n//2+1)):
        if visited[i] == 0:
            if i< n//2:
                if visited[i-1] != 0 or visited[i+1] != 0:
                    continue
            else:
                if visited[i-1] != 0:
                    continue
            visited[i] = 1
            solve(stage+1)
            visited[i] = 0

solve(0)
print(answer)
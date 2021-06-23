from heapq import *
# operations 10^6

def solution(operations):
    answer = []
    que = []
    for command in operations: # 10^6
        if command[0] == "I":
            num = int(command[2:])
            heappush(que,num)
        elif command[:3] == "D -":
            if len(que) >0:
                heappop(que)
        else:
            if len(que) >0:
                indexnum = que.index(nlargest(1, que)[0])
                que.pop(indexnum) # O(N)
    if len(que) > 0:
        front = que[0]
        behind = nlargest(1, que)
        answer = [behind[0],front]
    else:
        answer = [0,0]
    return answer

operations = ["I 16","D -1"]
solution(operations)
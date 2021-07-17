from heapq import *
from collections import deque

def solution(operations):
    answer = []
    operations = deque(operations)
    heapList = []
    while operations:
        operation = operations.popleft()
        if operation == "D -1":
            try:
                heapify(heapList)
                heappop(heapList)
            except:
                pass
        elif operation == "D 1":
            try:
                heapList = list(zip(list(map(lambda x : -x, heapList)),heapList))
                heapify(heapList)
                heappop(heapList)
                heapList = list(list(zip(*heapList))[1])
            except:
                pass
        else:
            num = int(operation.split()[-1])
            heapList.append(num)

    if not heapList:
        answer = [0,0]
    else:
        answer = [max(heapList), min(heapList)]
    return answer

#print(solution(["I 16","D 1"]),[0,0])
#print(solution(["I 7","I 5","I -5","D -1"]),[7,5])
#print(solution(["I 7","I 5","I -5","D 1"]),[7,5])
print(solution(["I 16","I -5643","D -1","D 1","D -1","I 123","D -1"]),[0, 0])
print(solution(["I -45","I 653","D 1","I -642","I 45","I 97","D 1","D -1","I 333"]),[333, -45])
#a = [1100,223,344,546,555]
#a = [7,5,-5]
#heapify(a)
#while a:
#    print(heappop(a))

#a = [1100,223,344,546,555]
#a = list(zip(list(map(lambda x : -x, a)), a))
#heapify(a)
#print(a)
#a = list(list(zip(*a))[1])
#print(a)
#while a:
#    print(heappop(a)[1])



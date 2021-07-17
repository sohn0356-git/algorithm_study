## 프린터
def solution(priorities, location):
    answer = 0
    n = len(priorities)
    locAndPri = list(zip([_ for _ in range(n)], priorities))
    
    count = 0
    while True:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            locAndPri.append(locAndPri.pop(0))
        else:
            count += 1
            priorities.pop(0)
            loc, pri = locAndPri.pop(0)
            if loc == location:
                answer = count
                break

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

# print([_ for _ in range(10)])
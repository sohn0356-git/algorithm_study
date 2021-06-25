def solution(n, lost, reserve):
    answer = 0
    students = dict()
    for i in range(1,n+1):
        if students.get(i) is None:
            students[i] = 1

    for elem in lost:
        students[elem] -= 1

    for elem in reserve:
        students[elem] += 1

    for student, clothes in students.items():
        if clothes == 0:
            if students.get(student-1) and students[student-1] == 2:
                students[student-1] -= 1
                students[student] += 1
            elif students.get(student+1) and students[student+1] == 2:
                students[student+1] -= 1
                students[student] += 1
    
    answer = n - list(students.values()).count(0)
    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
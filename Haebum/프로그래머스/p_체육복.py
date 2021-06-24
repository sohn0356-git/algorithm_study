def solution(n, lost, reserve):
    answer = -1
    student = [1] * (n+1)
    for i in lost:
        student[i] -= 1
    for a in reserve:
        student[a] += 1
    for j in range(len(student)):
        if j-1 > 0:
            if student[j-1] == 0 and student[j] > 1:
                student[j-1] += 1
                student[j] -= 1
        if j+1 <= n:
            if student[j+1] == 0 and student[j] > 1:
                student[j+1] += 1
                student[j] -= 1

    for k in student:
        if k >= 1:
            answer+=1
    print(answer)
    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
solution(n, lost, reserve)
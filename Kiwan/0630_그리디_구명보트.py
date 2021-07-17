def solution(people, limit):
    answer = 0
    rescue = []
    n = len(people)
    people.sort()
    a=1
    left = 0
    right = n-1
    while True:
        if left > right:
            break
        elif left == right:
            answer += 1
            break
        
        if people[left] + people[right] > limit:
            people[right] = 0
            right -= 1
            answer += 1
        else:
            people[right] = 0
            people[left] = 0
            right -= 1
            left += 1
            answer += 1
        
    return answer

print(solution([70, 50, 80, 50],100), 3)
print(solution([70, 50, 80],100), 3)
print(solution([40, 50, 60, 90], 100), 3)
print(solution([40, 40, 40], 100))
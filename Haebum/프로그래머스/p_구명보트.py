def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    maxP = n-1
    minP = 0
    while maxP != minP:
        if people[maxP] > 0:
            person1 = people[maxP]
        if people[minP] > 0:
            person2 = people[minP]
        if person1 + person2 <= limit:
            answer +=1
            people[maxP] = 0
            people[minP] = 0
            minP += 1
            maxP -= 1
        else:
            maxP -= 1
        
    for i in people:
        if i != 0:
            answer +=1
    return answer

people = [70, 50, 80, 50]
limit = 100
solution(people, limit)
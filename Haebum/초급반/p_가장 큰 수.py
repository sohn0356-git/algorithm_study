def solution(numbers):
    answer = ''

    numbers.sort(key = lambda x: (x%1000,x%100,x%10,x) if x//1000 >=1
    else (x%100,x%10,x) if x//100>=1
    else (x%10,x) if x//10 >=1
    else x if x>0, reverse=True)
    
    for i in numbers:
        answer += str(i)

    print(answer)
    return answer

numbers = [6, 10, 2]
solution(numbers)
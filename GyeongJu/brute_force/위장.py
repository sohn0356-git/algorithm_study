def solution(clothes):
    answer = 1
    dict = {}
    for cloth in clothes:
        if dict.get(cloth[1]):
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 2
    for k, v in dict.items():
        answer *= v
    answer -= 1
    return answer

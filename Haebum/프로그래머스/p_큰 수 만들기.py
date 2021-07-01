def solution(number, k):
    answer = ''
    emptyList = []
    emptyList.append(number[0]) # 초기값
    for num in number[1:]:
        while len(emptyList) > 0 and num > emptyList[-1] and k >0:
            emptyList.pop()
            k -=1
        emptyList.append(num)
    if k!=0:
        emptyList = emptyList[:-k]
    print(''.join(emptyList))
    answer = ''.join(emptyList)
    return answer

number = "4177252841"
k = 4
solution(number, k)
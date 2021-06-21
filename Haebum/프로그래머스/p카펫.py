def solution(brown, yellow):
    answer = []
    width = 0
    height = 0

    for i in range(1,yellow+1):
        if yellow%i == 0:
            if yellow/i >= i:
                height = i
                width = yellow//i

                if (width+2+height)*2 == brown:
                    answer.append(width+2)
                    answer.append(height+2)
    return answer

solution(24,24)
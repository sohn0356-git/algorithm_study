## 카펫
def solution(brown, yellow):
    answer = []
    width = None
    height = None

    for brown_width in range(3, int(brown / 2)):
        yellow_width = brown_width - 2
        if yellow % yellow_width == 0:
            height = yellow // yellow_width + 2
            width = yellow_width + 2
        if brown_width * 2 + (height - 2) * 2 == brown:
            break

    answer.append(height)
    answer.append(width)


    return answer
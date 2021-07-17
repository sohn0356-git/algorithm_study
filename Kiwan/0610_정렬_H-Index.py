## H-Index
def solution(citations):
    answer = 0
    h = 10000
    res = [0] * 1001
    n = len(citations)

    for j in range(1001):
        for i in range(n):
            if citations[i] >= j:
                res[j] += 1
        if res[j] == 0:
            break

    for k in range(1000, -1, -1):
        if res[k] == 0:
            continue
        h = k
        if res[k] >= h and n - res[k] <= h:
            break

        # h=6 6편이 상 인용된 논문이 1편 이상

    answer = h
    return answer
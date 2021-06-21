def solution(citations):
    answer = 0
    
    for i in range(1,1001):
        cnt = 0
        ncnt = 0
        for j in citations:
            if j >= i:
                cnt +=1
            else:
                ncnt += 1
        if i <= cnt:
            if ncnt <= i:
                answer = i
    return answer


#다른사람 풀이

def solution2(citations):
    answer = 0
    citations.sort()
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return answer

citations = [3, 0, 6, 1, 5]
print(solution2(citations))
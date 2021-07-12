#해시 이용한 풀이
def solution(clothes):
    answer = 1
    camouflage = dict()
    for value, key in clothes:
        if key in camouflage:
            camouflage[key].append(value)
        else:
            camouflage[key] = [value]
    for i in list(camouflage.values()):
        answer *= (len(i)+1)
    answer -=1
    print(answer)
    return answer

clothes = [["yellowhat", "headgear"],["whitehat", "headgear"],["eyedo", "eyedo"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)
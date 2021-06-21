## 위장
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["mask", "face"], ["redmask", "face"], ["abc", "pants"], ["abcd", "shirts"], ["abcsd", "socks"]]
def solution(clothes):
    answer = 0
    clotheList = dict()
    for i, clothe in enumerate(clothes):
        if clothe[1] not in clotheList.keys():
            clotheList[clothe[1]] = [clothe[0]]
        else:
            clotheList[clothe[1]].append(clothe[0])

    print(clotheList)
    temp = 1
    for key in clotheList.keys():
        temp *= (len(clotheList.get(key))+1)
    answer = temp-1
    return answer
print(solution(clothes))
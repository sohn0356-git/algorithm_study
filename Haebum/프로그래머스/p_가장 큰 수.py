def solution(numbers):
    # 스트링 변환하여 리스트 저장
    numbers = list(map(str,numbers))
    # 3자리수로 만들고 내림차순으로 정렬
    numbers.sort(key = lambda x: x*3, reverse=True)
    # 리스트에 있는 str을 이어서
    # 앞자리 0을 제거하기 위한 int로 변환 후 다시 str 변환 반환
    return str(int(''.join(numbers)))

numbers = [6, 10, 2]
print(solution(numbers))
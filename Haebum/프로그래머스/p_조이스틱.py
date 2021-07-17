def solution(name):  # 65~90(A~Z)
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    moves2 = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    pos = 0
    answer = 0
    while True:
        answer += moves[pos]
        moves[pos] = 0

        if sum(moves) == 0: break

        left = 1
        right = 1

        while moves[pos - left] == 0:
            left += 1

        while moves[pos + right] == 0:
            right += 1

        if left >= right:
            pos += right
            answer += right
        else:
            pos -= left
            answer += left

    pos2 = 0
    answer2 = 0
    while True:
        answer2 += moves2[pos2]
        moves2[pos2] = 0

        if sum(moves2) == 0: break

        left = 1
        right = 1

        while moves2[pos2 - left] == 0:
            left += 1

        while moves2[pos2 + right] == 0:
            right += 1

        if left > right:
            pos2 += right
            answer2 += right
        else:
            pos2 -= left
            answer2 += left

    answer = min(answer,answer2)
    print(answer)
    return answer

name = "ABBAAAAAB"
name2 = "ABAAAABB"
solution(name2)
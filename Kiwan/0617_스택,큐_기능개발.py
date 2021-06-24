## 기능개발
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    top = 0
    while True:
        for i in range(n):
            if progresses[i] >= 100:
                continue
            else:
                progresses[i] += speeds[i]
        # print(progresses)

        if progresses[top] >= 100:
            chk = 0
            while True:
                if top >= n:
                    break

                if progresses[top] >= 100:
                    top += 1
                    chk += 1
                else:
                    break
            answer.append(chk)

        if top >= n:
            break
    # print(answer)
    return answer

progresses = [93, 30, 55]#[95, 90, 99, 99, 80, 99]
speeds = [1, 30, 5]#[1, 1, 1, 1, 1, 1]
solution(progresses, speeds)
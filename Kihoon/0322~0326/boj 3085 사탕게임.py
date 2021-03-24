
def bomboni(board):
    for j in range(N):
        for i in range(N-1):
            if board[j][i] != board[j][i+1]:  #가로 검사
                board[j][i] , board[j][i+1] = board[j][i+1], board[j][i]
                checkanswer(board)
                board[j][i], board[j][i+1] = board[j][i+1], board[j][i]

            if board[i][j] != board[i+1][j]: #세로검사
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                checkanswer(board)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

def checkanswer(boardcheck):
    global answer
    for j in range(N):
        verticnt = 1 #0으로 초기화하면 자기 자신을 안세버림
        horicnt = 1
        for i in range(N-1):
            if boardcheck[i][j] == boardcheck[i+1][j]: #세로로 같은거 세기
                verticnt +=1
            else:
                if answer < verticnt:
                    answer = verticnt
                verticnt = 1
            if boardcheck[j][i] == boardcheck[j][i+1]: #가로로 세기
                horicnt +=1
            else:
                if answer < horicnt:
                    answer = horicnt
                horicnt = 1

        if answer < horicnt:
            answer = horicnt
        if answer < verticnt:
            answer = verticnt



N = int(input())
board = []

for _ in range(N):
    board.append(list(input()))

answer = 0

bomboni(board)

print(answer)
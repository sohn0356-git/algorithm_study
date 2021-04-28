#최대값 1000*5
#브루트포스로 풀예정
#n과 m 형태로 풀 예정이고 입력순서가 상담날짜
# 그에따른 리스트형태로 상담기간과 이익을 담을 예정
#시간복잡도 n은 15가 최대이므로 15**15..? 안됨
#공간복잡도는 list덱 4*2*15 visited 15*4 = 120+90 = 210*15 얼마 안됨...

#두번째 풀이
# 생각이 안나므로 1번풀이 일단 풀어봄..

# n과 m으론 못풀겠음..

# n = int(input())
# counseling = [0]*(n+1)
# today = 0
# benefit = 0
# for idx in range(1,n+1):
#     counseling[idx] = list(map(int,input().split()))
# visited = [0]*(n+1)
# def solve(stage):
#     if  max(visited) > n:

#         for i in range(n):
#             if visited[i] == 1:
#                 today += counseling[i][0]
#         break

#     for i in range(1,n+1):
#         if max(visited) >i:
#             continue
#         if visited[i] == 0:
#             visited[i] += counseling[i][0]
#             solve(stage+1)
#             visited[i] = 0
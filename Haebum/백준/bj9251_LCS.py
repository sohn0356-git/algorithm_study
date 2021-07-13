# DP풀이

import sys
# text1 = ' '+ sys.stdin.readline().rstrip()
# text2 = ' ' + sys.stdin.readline().rstrip()
# LCS = [[0]*len(text2) for _ in range(len(text1))]
# for i in range(1,len(text1)):
#     for j in range(1,len(text2)):
#         if text1[i] == text2[j]:
#             LCS[i][j] = LCS[i-1][j-1] +1
#         else:
#             LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
    
# print(LCS[-1][-1])


text1 = sys.stdin.readline().rstrip()
text2 = sys.stdin.readline().rstrip()
LCS = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
for i in range(1,len(text1)+1):
    for j in range(1,len(text2)+1):
        if text1[i-1] == text2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
    
print(LCS[-1][-1])

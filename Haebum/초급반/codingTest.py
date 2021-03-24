a = [1,2,[4,5,6]]
b= a   #shallow copy
print(b) # [1,2,3]
b[1] = 3    # b의 1번자리를 3으로 변경
print(b) # [1,3,3]
b[2]
print(a) # [1,3,3] b를 변경했지만 a도 같이 변경됨!

import copy

a = [1,2,[4,5,6]]
b = copy.deepcopy(a)
print(b)
b[1] = 2
print(b)
print(a)
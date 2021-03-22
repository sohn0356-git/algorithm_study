# 문제
# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.
#
# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

###성공
# def mul(A, B, C):
#     global res;
#     if B == 1:
#         res[B - 1] = A % C;
#     else:
#         # print(B);
#         if res.get(B - 1) == None:
#             if B % 2 == 0:
#                 res[B - 1] = (mul(A, B // 2, C) * mul(A, B // 2, C)) % C;
#             else:
#                 res[B - 1] = (mul(A, B // 2, C) * mul(A, B // 2, C) * A) % C
#     return res.get(B - 1) % C;

def mul(A, B, C):
    if B <= 1:
        return A % C;
    else:
        if B % 2 == 0:
            return (mul(A, B // 2, C) * mul(A, B // 2, C)) % C;
        else:
            return (mul(A, B // 2, C) * mul(A, B // 2, C) * A) % C

A, B, C = map(int, input().split());
res = dict();
print(mul(A, B, C));

# #include <iostream>
# #include <sstream>
# #include <string>
# #include <cmath>
# #include <algorithm>
# #include <vector>
# using namespace std;
#
# int main()
# {
#   long long a, b, c, A, B, C = 1;
#   cin >> a >> b >> c;
#   A = a % c;
#   B = b;
#   while (B != 1){
#       if (B % 2 != 0){
#       C = A * C % c;
#       }
#           A = A * A % c;
#           B /= 2;
#   }
#   cout << A * C % c;
#
# }
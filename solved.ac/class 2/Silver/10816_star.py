# 10816번 숫자 카드 2
# 해시값으로 풀었지만
# 이분탐색으로도 풀어보기 !

import sys
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))
n_dic = {}

for i in n_arr:
    if i not in n_dic:
        n_dic[i] = 1
    else:
        n_dic[i] += 1

# join 사용
print(' '.join(str(n_dic[m]) if m in n_dic else '0' for m in m_arr))
            
# 시간 초과
# import sys
# input = sys.stdin.readline

# N = int(input())
# n_arr = list(map(int, input().split()))
# M = int(input())
# m_arr = list(map(int, input().split()))
# n_dic = {}
# result = []
# for i in n_arr:
#     if i not in n_dic:
#         n_dic[i] = 1
#     else:
#         n_dic[i] += 1

# for i in m_arr:
#     try:
#         if m_arr.index(i) == M-1:
#             print(n_dic[i],end="")
#         else:
#             print(n_dic[i],end=" ")
#     except:
#         if m_arr.index(i) == M-1:
#             print(0,end="")
#         else:
#             print(0,end=" ")
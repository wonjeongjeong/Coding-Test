# 10989번 수 정렬하기 3
# 계수 정렬 사용
import sys
input = sys.stdin.readline

N = int(input())
num_list = [0]*(10001)

for i in range(N):
    num = int(input())
    num_list[num] += 1
    
for i in range(len(num_list)):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
            
# 시간 초과
# N = int(input())
# num_list = []

# for i in range(N):
#     insert = False
#     num = int(input())
#     if i == 0:
#         num_list.append(num)
#         median = num
#     else:
#         if median > num:
#             for j in range(num_list.index(median)+1):
#                 if num <= num_list[j]:
#                     num_list.insert(j, num)
#                     median = num_list[len(num_list) // 2]
#                     break
#         elif median == num:
#             equal = num_list.index(median)
#             num_list.insert(equal, num)
#             median = num_list[len(num_list) // 2]
#         else:
#             for j in range(num_list.index(median)+1,i):
#                 if num <= num_list[j]:
#                     num_list.insert(j, num)
#                     median = num_list[len(num_list) // 2]
#                     insert = True
#                     break
#             if insert == False:
#                 num_list.append(num)
#                 median = num_list[len(num_list) // 2]

# for i in range(N):
#     print(num_list[i])
    
# 시간초과 
# N = int(input())
# num_list = []

# for i in range(N):
#     num = int(input())
#     insert = False
#     if i == 0:
#         num_list.append(num)
#         insert = True
#     else:
#         for j in range(i):
#             if num <= num_list[j]:
#                 num_list.insert(j, num)
#                 insert = True
#                 break
#         if insert == False:
#             num_list.append(num)

# for i in range(N):
#     print(num_list[i])
# 2751번 수 정렬하기 2
import sys
input = sys.stdin.readline

N = int(input())
num_list = [False] * (2000001)

for i in range(N):
    num = int(input())
    num_list[num+1000000] = True
         
for i in range(2000001):
    if num_list[i] == True:
        print(i - 1000000)
    
# 시간 초과
# N = int(input())
# num_list = []

# for i in range(N):
#     num = int(input())
#     num_list.append(num)
    
# num_list.sort()

# for i in range(N):
#     print(num_list[i])

# 시간 초과
# N = int(input())
# positive = [0]*1000001
# negative = [0]*1000001

# for i in range(N):
#     num = int(input())
#     if num < 0:
#         negative[abs(num)] = 1
#     else:
#         positive[num] = 1

# for i in range(1000000, 0, -1):
#     if negative[i] == 1:
#         print("-",end="")
#         print(i)
# for i in range(1000001):
#     if positive[i] == 1:
#         print(i)
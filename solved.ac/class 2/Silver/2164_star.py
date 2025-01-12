# 2164번 카드2
# 정석은 큐 자료구조 쓰는 것 !!! 
# 큐로 다시 한 번 풀어보기
import math

N = int(input())
num = 2**math.floor(math.log2(N))
last_card = (N-num) * 2
if last_card == 0:
    print(N)
else:
    print(last_card)


# 시간초과
# N = int(input())
# if N == 1:
#     print(1)
# elif N == 2 or N == 3:
#     print(2)
# else:
#     arr = [i for i in range(2, N+1, 2)]
#     if N % 2 == 0:
#         while len(arr) > 1:
#             del arr[0]
#             next = arr.pop(0)
#             arr.append(next)

#     else:
#         while len(arr) > 1:
#             next = arr.pop(0)
#             arr.append(next)
#             del arr[0]
        
#     print(arr[0])
    
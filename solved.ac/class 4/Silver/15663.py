# 15663번 N과 M (9)
from itertools import permutations
N, M = map(int, input().split())

arr = list(map(int, input().split()))

total = list(set(permutations(arr, M))) # set으로 중복 제거
total = sorted(total)

for i in range(len(total)):
    for j in range(M):
        print(total[i][j],end=' ')

    print("")
    
# 시간 초과과
# from itertools import permutations
# N, M = map(int, input().split())

# arr = list(map(int, input().split()))
    
# arr = sorted(arr)
# total = list(i for i in permutations(arr, M))
# total_copy = list(i for i in permutations(arr, M))

# for idx in range(len(total)):
#     twin = total[idx]
#     if twin in total[idx+1:]:
#         total_copy.remove(twin)
        

# for i in range(len(total_copy)):
#     for j in range(M):
#         print(total_copy[i][j],end=' ')

#     print("")
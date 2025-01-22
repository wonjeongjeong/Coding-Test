# 9375번 패션왕 신해빈
T = int(input())

for i in range(T):
    types = []
    duplicate = {}
    
    N = int(input())
    for j in range(N):
        _, type = map(str, input().split())
        if type in types:
            duplicate[type] += 1
        else:
            types.append(type)
            duplicate[type] = 1
            
    result = 1
    for k in types:
        result *= (duplicate[k] + 1) # 안 입는 경우인 0 추가
        
    print(result-1) # 전부 0일 경우 (아무것도 입지 않은 경우) 제외
    
# 시간초과
# from itertools import combinations
# T = int(input())

# for i in range(T):
#     types = []
#     duplicate = {}
    
#     N = int(input())
#     for j in range(N):
#         _, type = map(str, input().split())
#         if type in types:
#             duplicate[type] += 1
#         else:
#             types.append(type)
#             duplicate[type] = 1
    
#     result = N
#     for t in range(2, len(types)+1):
#         test = 1
#         for k in combinations(types, t):
#             for s in k:
#                 test *= duplicate[s]
                
#             result += test
    
#     print(result)
    
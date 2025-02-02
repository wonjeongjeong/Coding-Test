# 11660번 구간 합 구하기 5
# 누적합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0]*(N+1) for _ in range(N+1)]

# 누적합 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = arr[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(result)


# 시간초과
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# arr = []
# for i in range(N):
#     line = list(map(int, input().split()))
#     arr.append(line)
    
# for i in range(M):
#     sum = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     for a in range(x1-1, x2):
#         for b in range(y1-1, y2):
#             sum += arr[a][b]
    
#     print(sum)
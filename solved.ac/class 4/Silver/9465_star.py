# 9465번 스티커

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    # DP 테이블 초기화
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[0][0] + sticker[1][1]

    # DP 점화식 적용
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))
    
# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     sticker = []
    
#     n = int(input())
#     score_arr = []
#     for _ in range(2):
#         line = list(map(int, input().split()))
#         sticker.append(line)
    
#     if n == 1:
#             print(max(sticker[0][0], sticker[1][0]))
#     elif n == 2:
#             print(max(sticker[0][0] + sticker[1][1], sticker[1][0] + sticker[0][1]))
#     else:    
#         for a in range(2):
#             b = 0
#             score = sticker[a][0]
#             while b < n-2:
#                 if a == 0:
#                     max_score = max(sticker[a][b+2] + sticker[a+1][b+1], sticker[a+1][b+2])
#                     if max_score == sticker[a+1][b+2]:
#                         a = a + 1
#                     b = b + 2
                        
#                 else:
#                     max_score = max(sticker[a][b+2] + sticker[a-1][b+1], sticker[a-1][b+2])
#                     if max_score == sticker[a-1][b+2]:
#                         a = a - 1
#                     b = b + 2
                      
#                 score += max_score
                    
#             score_arr.append(score)
                
#         print(max(score_arr))
    

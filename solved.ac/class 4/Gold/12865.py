# 12865번 평범한 배낭
# 냅색 알고리즘
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

weight_value_list = [[0, 0]]
for i in range(N):
    weight_value_list.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = weight_value_list[i][0]
        value = weight_value_list[i][1]
        
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            
print(dp[N][K])
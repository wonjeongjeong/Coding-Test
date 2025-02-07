# 1932번 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    dp.append([0]*(i+1))
    
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+arr[i][j], dp[i-1][j]+arr[i][j])
            
print(max(dp[n-1]))

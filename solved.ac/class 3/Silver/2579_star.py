# 2579번 계단 오르기
import sys
input = sys.stdin.readline

n = int(input().strip())
stair = [int(input().strip()) for _ in range(n)]
score = [0] * n

if len(stair) <= 2:
    print(sum(stair))
else:
    score[0] = stair[0]
    score[1]= stair[0] + stair[1]
    for i in range(2, n):
        score[i] = max(score[i-3] + stair[i-1] + stair[i], score[i-2] + stair[i]) 
    print(score[-1])


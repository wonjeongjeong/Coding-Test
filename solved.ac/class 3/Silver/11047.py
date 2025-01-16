# 11047번 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
judge = False

for i in range(N):
    coin = int(input().strip())
    coins.append(coin)
    
remain = K
count = 0

for i in range(N-1, -1, -1):
    if remain == 0:
        break
    else:
        count += remain // coins[i]
        remain %= coins[i]
    
print(count)
    
    
    
# 11659번 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0] * (N+1)
sum_arr[1] = arr[0]
for i in range(2, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

for i in range(M):
    a, b = map(int, input().split())
    result = sum_arr[b] - sum_arr[a-1]
    print(result)
    
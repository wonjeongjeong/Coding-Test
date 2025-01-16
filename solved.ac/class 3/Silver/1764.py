# 1764번 듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

listen = {}
arr = []

for i in range(N):
    name = input().strip()
    listen[name] = 1

for i in range(M):
    name = input().strip()
    try:
        if listen[name] == 1:
            arr.append(name)
    except:
        continue

arr.sort()
print(len(arr))
for name in arr:
    print(name)
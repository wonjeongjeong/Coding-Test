# 11399번 ATM
import sys
input = sys.stdin.readline

N = int(input().strip())

P = list(map(int, input().split()))

P.sort()

time = 0
for i in range(N+1):
    person = 0
    for j in range(i):
        person += P[j]
    time += person
print(time)
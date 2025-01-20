# 2606번 바이러스
from collections import deque
N = int(input())
connect = int(input())
computer = [[] for i in range(N+1)]
tf = [0] * (N+1)
for i in range(connect):
    a, b = map(int, input().split())
    computer[a] += [b]
    computer[b] += [a]

tf[1] = 1
Q = deque([1])

while Q:
    c=Q.popleft()
    for i in computer[c]:
        if tf[i] == 0:
            Q.append(i)
            tf[i] = 1
            
print(sum(tf)-1) 
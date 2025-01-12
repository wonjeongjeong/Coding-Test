# 11866번 요세푸스 문제 0
from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))
arr = []

while len(queue) > 0:
    for i in range(K):
        if i == K-1:
            remove = queue.popleft()
            arr.append(remove)
        else:
            back = queue.popleft()
            queue.append(back)

print("<", end="")
print(", ".join(map(str, arr)), end="")
print(">")
            
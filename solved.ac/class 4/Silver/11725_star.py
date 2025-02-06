# 11725번 트리의 부모 찾기
# DFS 활용
import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node):
    for child in tree[node]:
        if parent[child] == 0:
            parent[child] = node
            dfs(child)

parent[1] = 1 
dfs(1)

for i in range(2, N + 1):
    print(parent[i])
    
# N = int(input())
# parent = [0] * (N+1)
# for i in range(N-1):
#     a, b = map(int, input().split())
#     if a == 1:
#         parent[b] = a
#     elif b == 1:
#         parent[a] = b
#     else:
#         if parent[a] != 0:
#             parent[b] = a
        
#         elif parent[b] != 0:
#             parent[a] = b

# for i in range(2, N+1):
#     print(parent[i])
        
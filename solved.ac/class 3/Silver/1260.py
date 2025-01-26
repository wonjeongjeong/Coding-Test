# 1260번 DFS와 BFS
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

def DFS(g, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(g[v]):
        if not visited[i]:
            DFS(g,i,visited)
            
def BFS(g, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in sorted(g[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_d = [False] * (N+1)
visited_b = [False] * (N+1)
 
DFS(graph, V, visited_d)
print("")
BFS(graph, V, visited_b)
    
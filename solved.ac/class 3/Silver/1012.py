# 1012번 유기농 배추
# 너비 우선 탐색

import sys
input = sys.stdin.readline

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] # 상, 하, 좌, 우

def BFS(x,y):
    queue = [(x,y)]
    arr[x][y] = 0
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0
                
for i in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    count = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X][Y] = 1
        
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                BFS(i, j)
                count += 1
                
    print(count)

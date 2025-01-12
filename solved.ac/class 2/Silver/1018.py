# 1018번 체스판 다시 칠하기
N, M = map(int, input().split())
chess = [['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W']]
board = []

for i in range(N):
    line = list(input())
    board.append(line)
    
count1 = 0
count2 = 0
result = []
for i in range(N-7):
    for j in range(M-7):
        x = 0
        for a in range(i, i+8):
            y = 0
            for b in range(j, j+8):
                if board[a][b] != chess[x][y]:
                    count1 += 1
                if board[a][b] == chess[x][y]:
                    count2 += 1
                y += 1
            x += 1
        result.append(min(count1, count2))
        count1 = 0
        count2 = 0
print(min(result))
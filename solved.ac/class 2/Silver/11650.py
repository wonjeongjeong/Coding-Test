# 11650번 좌표 정렬하기
N = int(input())
points = []

for i in range(N):
    point = list(map(int, input().split()))
    points.append(point)
    
sort_point = sorted(points, key = lambda x: (x[0], x[1]))

for i in range(N):
    print(f"{sort_point[i][0]} {sort_point[i][1]}")


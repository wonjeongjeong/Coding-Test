# 15650번 N과 M (2)
import itertools
N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
total = list(itertools.combinations(arr, M))

for i in range(len(total)):
    for j in range(M):
        print(total[i][j],end=' ')
    print("")
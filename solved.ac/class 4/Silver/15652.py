# 15652번 N과 M (4)
from itertools import combinations_with_replacement
N, M = map(int, input().split())

total = list(i for i in combinations_with_replacement(range(1, N+1), M))

for i in range(len(total)):
    for j in range(M):
        print(total[i][j],end=' ')
    print("")
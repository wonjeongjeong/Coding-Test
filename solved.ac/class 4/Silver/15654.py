# 15654번 N과 M (5)
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
total = list(i for i in permutations(arr, M))

for i in range(len(total)):
    for j in range(M):
        print(total[i][j],end=' ')
    print("")
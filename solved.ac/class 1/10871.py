# 10871번 X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []

for i in range(N):
    if X > A[i]:
        result.append(A[i])
        
for i in range(len(result)):
    if i == len(result) - 1:
        print(f"{result[i]}",end="")
    else:
        print(f"{result[i]} ",end="")
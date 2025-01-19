# 1463번 1로 만들기
N = int(input())
arr = [0] * 1000001
arr[1] = 0

for i in range(2, N+1):
    arr[i] = arr[i-1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i//2] + 1, arr[i])
    if i % 3 == 0:
        arr[i] = min(arr[i//3] + 1, arr[i])
        
print(arr[N])
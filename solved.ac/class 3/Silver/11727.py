# 11727번 2xn 타일링 2
N = int(input())

arr = [0] * 1001

arr[1] = 1
arr[2] = 3

for i in range(3, 1001):
    arr[i] = arr[i-1] + arr[i-2] * 2
    
result = arr[N] % 10007
print(result)
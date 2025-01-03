# 10818번 최소, 최대
n = int(input())

num = list(map(int, input().split()))
min = num[0]
max = num[0]

for i in range(1, n):
    if min > num[i]:
        min = num[i]
    if max < num[i]:
        max = num[i]
        
print(f"{min} {max}")
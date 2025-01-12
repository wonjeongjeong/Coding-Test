# 2839번 설탕 배달
N = int(input())
kg_5 = N // 5
kg_3 = N // 3
arr = []
for i in range(kg_5+1):
    for j in range(kg_3+1):
        if i*5 + j*3 == N:
            box = i + j
            arr.append(box)
            
if len(arr) > 0:
    print(min(arr))
else:
    print(-1)
    
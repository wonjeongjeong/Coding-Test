# 1654번 랜선 자르기
K, N = map(int, input().split())
total = 0
arr = []
for i in range(K):
    lan = int(input())
    total += lan
    arr.append(lan)
    
low = 1
high = max(arr)
result = 0
while high >= low:
    counts = 0
    mid = (low+high) // 2
    for lan in arr:
        count = lan // mid
        counts += count
    if counts >= N:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)

# 시간 초과
# K, N = map(int, input().split())
# total = 0
# arr = []
# for i in range(K):
#     lan = int(input())
#     total += lan
#     arr.append(lan)
    
# min_length = min(arr)

# length = total // N
# counts = 0

# if length > min_length:
#     length = min_length
    
# while counts < N:
#     counts = 0
#     for lan in arr:
#         count = lan // length
#         counts += count
#     length -= 1
    
# print(length)
    
    
    
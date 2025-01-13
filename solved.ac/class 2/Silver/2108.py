# 2108번 통계학
import sys
input = sys.stdin.readline

def half_round(x):
    if x >= 0:
        if x - int(x) >= 0.5:
            return int(x) + 1
        else:
            return int(x)
    else:
        if x - int(x) <= -0.5:
            return int(x) - 1
        else:
            return int(x)
    
N = int(input().strip())
counts = [0] * 8001
arr = []
total = 0
for i in range(N):
    num = int(input().strip())
    arr.append(num)
    counts[num + 4000] += 1
    total += num

average = half_round(total / N)
count = 0
for i in range(len(counts)):
    if counts[i] != 0:
        count += counts[i]
        if count > N//2:
            middle = i - 4000
            break
print(average)
print(middle)
again = []
for i in range(len(counts)):
    if counts[i] != 0:
        if counts[i] == max(counts):
            again.append(i - 4000)
            
if len(again) > 1:
    print(again[1])
else:
    print(again[0])

print(max(arr)-min(arr))
            

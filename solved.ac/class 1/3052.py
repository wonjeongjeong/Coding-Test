# 3052번 나머지
num = []
remain = [0 for _ in range(42)]
count = 0

for _ in range(10):
    n = int(input())
    num.append(n)

for i in range(10):
    r = num[i] % 42
    remain[r] = 1
    
for i in range(42):
    if remain[i] == 1:
        count += 1
        
print(count)
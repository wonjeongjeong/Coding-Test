# 30802번 웰컴 키트
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
T_order = 0

for i in range(6):
    if size[i] % T == 0:
        count = size[i] // T
    else:
        count = size[i] // T + 1
    T_order += count
    
P_order = N // P
remain = N % P

print(T_order)
print(f"{P_order} {remain}")


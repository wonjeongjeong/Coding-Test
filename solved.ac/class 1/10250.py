# 10250번 ACM 호텔
T = int(input())
list_H = []
list_W = []
list_N = []

for i in range(T):
    H, W, N = map(int, input().split())
    list_H.append(H)
    list_W.append(W)
    list_N.append(N)
    
for i in range(T):
    line = list_N[i] // list_H[i] + 1
    floor = list_N[i] % list_H[i]
    
    if floor == 0:
        line = line - 1
        floor = list_H[i]
        
    if line < 10:
        print(f"{floor}0{line}")
    else:
        print(f"{floor}{line}")
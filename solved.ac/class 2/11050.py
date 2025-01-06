# 11050번 이항 계수
N, K = map(int, input().split())
top = 1
bottom = 1
x = K
for i in range(K):
    top *= N
    N -= 1
    
for i in range(K):
    bottom *= x
    x -= 1
    
result = top // bottom
print(result)
    

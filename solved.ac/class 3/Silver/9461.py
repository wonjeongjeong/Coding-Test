# 9461번 파도반 수열
T = int(input())
P = [0] * 101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2

def triangle(n):
    if P[n] == 0:  # 아직 계산되지 않은 경우
        P[n] = triangle(n-1) + triangle(n-5)
    return P[n]

for _ in range(T):
    N = int(input())
    print(triangle(N))

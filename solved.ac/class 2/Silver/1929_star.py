# 1929번 소수 구하기
# 에라토스테네스의 체
M, N = map(int, input().split())
is_prime = [True for _ in range(N+1)]
is_prime[1] = False
p = 2
while (p * p < N + 1):
    if is_prime[p]:
        for i in range(p*p, N+1, p):
            is_prime[i] = False
    p += 1

for num in range(M, N+1):
    if is_prime[num]:
        print(num)

# 1978번 소수 찾기
N = int(input())

num = list(map(int, input().split()))

result = 0

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

for i in range(N):
    if num[i] == 1:
        continue
    elif num[i] == 2:
        result += 1
    else:
        if is_prime_num(num[i]):
            result += 1
    
print(result)
    
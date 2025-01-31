# 1629번 곱셈
# 분할정복을 이용한 거듭제곱
A, B, C = map(int, input().split())

def iterative_power(a, n):
    result = 1
    while n > 0:
        # n이 홀수인 경우, 결과에 a를 곱하고 n을 하나 감소
        if n % 2 == 1:
            result *= a
        # a를 제곱하고 n을 반으로 줄임
        a *= a
        a = a%C
        n //= 2
    return result

result = iterative_power(A, B) % C
print(result)
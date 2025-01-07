# 2609번 최대공약수와 최소공배수
A, B = map(int, input().split())

# 유클리드 호제법으로 최대공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
        
# 최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누어 구할 수 있다.
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(A, B))
print(lcm(A, B))
# 15829번 Hashing
# 50점 (1234567891 로 안 나눠줘서...)
# 100점

L = int(input())
string = input()
result = 0

for i in range(L):
    num = ord(string[i]) - ord('a') + 1
    result += num * (31**i)

print(result % 1234567891)
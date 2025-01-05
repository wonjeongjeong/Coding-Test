# 15829번 Hashing
# 50점

L = int(input())
string = input()
result = 0

for i in range(L):
    num = ord(string[i]) - ord('a') + 1
    result += num * (31**i)

print(result)
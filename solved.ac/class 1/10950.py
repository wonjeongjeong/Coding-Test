# 10950번 A+B -3
t = int(input())
list_a = []
list_b = []
for i in range(t):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

for i in range(t):
    print(list_a[i] + list_b[i])
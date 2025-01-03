# 2675번 문자열 반복
t = int(input())
r = []
s = []

for i in range(t):
    input_list = input().split()
    r.append(int(input_list[0]))
    s.append(input_list[1])
    
for i in range(t):
    for word in s[i]:
        print(word*r[i], end="")
    print("\n", end="")
# 8958번 OX퀴즈
T = int(input())
ans_list = []

for i in range(T):
    ans = input()
    ans_list.append(ans)
    
for i in range(T):
    total = 0
    score = 0
    for answer in ans_list[i]:
        if answer == "O":
            score += 1
        else:
            score = 0
            
        total += score
        
    print(total)
        
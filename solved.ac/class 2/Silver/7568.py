# 7568번 덩치
N = int(input())
group = []
rank = []

for i in range(N):
    person = list(map(int, input().split()))
    group.append(person)
    
for i in range(N):
    k = 0
    for j in range(N) :
        if j == i:
            continue
        else:
            if group[i][0] < group[j][0]:
                if group[i][1] < group[j][1]:
                    k += 1
    if i == N-1:                
        print(k+1,end="")
    else:
        print(k+1,end=" ")
    

    
    
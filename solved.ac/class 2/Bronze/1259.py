# 1259번 팰린드롬수
while True:
    num = list(input())
    if num == ['0']:
        break
    re_num = ['1' for _ in range(len(num))]
    
    for i in range(len(num)):
        re_num[i] = num[len(num) - 1 - i]
        
    if num == re_num:
        print("yes")
    else:
        print("no")
# 2292번 벌집
N = int(input())

def count(x):
    sum = 0
    num = 0
    zero = False
    while True:
        num += 1
        sum += num
        if sum > x:
            return num, zero
        elif sum == x:
            zero = True
            return num, zero

if N == 1:
    print("1")
else:        
    x = (N-1) // 6
    v = (N-1) % 6
    num, zero = count(x)
    # 몫만 따지면 1+2+3+... 합에 딱 떨어지는 수인데
    # 나머지가 있는 경우만 +2 를 해줌
    if v != 0 and zero == True:
        print(num + 2)
    else:
        print(num + 1)
            
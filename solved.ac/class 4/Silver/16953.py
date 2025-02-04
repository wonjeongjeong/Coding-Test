# 16953번 A -> B
A, B = map(int, input().split())
temp = B
count = 1
count_print = True
while True:
    if temp == A:
        break
    elif temp < A:
        print("-1")
        count_print = False
        break
    else:
        if temp % 2 == 0:
            temp = temp // 2
            count += 1
        else:
            if str(temp)[-1] == '1':
                temp = int(str(temp)[:-1])
                count += 1
            else:
                print("-1")
                count_print = False
                break

if count_print == True:
    print(count)
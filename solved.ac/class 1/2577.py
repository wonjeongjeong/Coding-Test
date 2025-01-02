number = []
for i in range(3):
    n = int(input())
    number.append(n)
    
result = number[0] * number[1] * number[2]
result = str(result)

count = [0]*10
for s in result:
    if s == "0":
        count[0] += 1
    elif s == "1":
        count[1] += 1
    elif s == "2":
        count[2] += 1
    elif s == "3":
        count[3] += 1
    elif s == "4":
        count[4] += 1
    elif s == "5":
        count[5] += 1
    elif s == "6":
        count[6] += 1
    elif s == "7":
        count[7] += 1
    elif s == "8":
        count[8] += 1
    else:
        count[9] += 1

for i in range(len(count)):
    print(count[i])

    
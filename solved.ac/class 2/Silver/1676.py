# 1676번 팩토리얼 0의 개수
N = int(input())
count = 0
def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    
    return result

string = str(factorial(N))
for i in range(len(string)-1, -1, -1):
    if string[i] == '0':
        count += 1
    else:
        break
    
print(count)
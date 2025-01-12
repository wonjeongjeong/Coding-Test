# 10773번 제로
K = int(input())
stack = []
for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
sum = 0
for i in range(len(stack)):
    sum += stack[i]
    
print(sum)
# 9012번 괄호
T = int(input())
for i in range(T):
    line = input()
    stack = []
    balance = True
    for word in line:
        if word == "(":
            stack.append(word)
        else:
            if len(stack) == 0:
                balance = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                break
    
    if len(stack) == 0 and balance == True:
        print("YES")
    else:
        print("NO")
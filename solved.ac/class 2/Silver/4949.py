# 4949번 균형잡힌 세상
# 스택
while True:
    line = input()
    if line == ".":
        break
    stack = []
    balance = True
    for word in line:
        if word == "[":
            stack.append(word)
        elif word == "(":
            stack.append(word)
        elif word == "]":
            if len(stack) == 0:
                balance = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                break
        elif word == ")":
            if len(stack) == 0:
                balance = False
                break
            if stack[-1] == "(":
                stack.pop()
            else:
                break
    
    
    if len(stack) == 0 and balance == True:
        print("yes")
    else:
        print("no")
    
            
            
    
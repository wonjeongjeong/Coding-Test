# 10828번 스택
import sys
input = sys.stdin.readline

N = int(input().strip())

stack = []

for i in range(N):
    command = input().strip()
    length = len(stack)
    if command == "pop":
        if length>0:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(length)
    elif command == "empty":
        if length>0:
            print(0)
        else:
            print(1)
    elif command == "top":
        if length>0:
            print(stack[-1])
        else:
            print(-1)
    else:
        X = command[5:]
        stack.append(int(X))
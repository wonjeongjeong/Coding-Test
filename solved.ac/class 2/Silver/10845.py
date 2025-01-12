# 10845번 큐
import sys
input = sys.stdin.readline

N = int(input().strip())

queue = []

for i in range(N):
    command = input().strip()
    length = len(queue)
    if command == "pop":
        if length>0:
            print(queue.pop(0))
        else:
            print(-1)
    elif command == "size":
        print(length)
    elif command == "empty":
        if length>0:
            print(0)
        else:
            print(1)
    elif command == "front":
        if length>0:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if length>0:
            print(queue[-1])
        else:
            print(-1)
    else:
        X = command[5:]
        queue.append(int(X))
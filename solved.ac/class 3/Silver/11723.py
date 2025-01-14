# 11723번 집합
import sys
input = sys.stdin.readline
S = []

M = int(input().strip())

for i in range(M):
    order = input().strip()
    if order == "all":
        S = [i for i in range(1, 21)]
    elif order == "empty":
        S = []
    else:
        cal, x = map(str, order.split())
        x = int(x)
        if x in S:
            be = True
        else:
            be = False
        if cal == "add":
            if be == True:
                continue
            else:
                S.append(x)
        elif cal == "remove":
            if be == False:
                continue
            else:
                S.remove(x)
        elif cal == "check":
            if be == True:
                print(1)
            else:
                print(0)
        elif cal == "toggle":
            if be == True:
                S.remove(x)
            else:
                S.append(x)
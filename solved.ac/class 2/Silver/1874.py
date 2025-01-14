# 1874번 스택 수열
n = int(input())
arr = []
stack = []
input_arr = [0]
sign = []
yes = True

for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    if input_arr[-1] < arr[i]:
        for j in range(input_arr[-1]+1, arr[i]+1):
            stack.append(j)
            input_arr.append(j)
            sign.append("+")
        stack.pop()
        sign.append("-")
    else:
        if stack[-1] == arr[i]:
            stack.pop()
            sign.append("-")
        else:
            print("NO")
            yes = False
            break

if yes == True:
    for i in range(len(sign)):
        print(sign[i])  
        
# n = int(input())
# arr = []
# stack = []
# check = [False] * (n+1)
# check[0] = True
# for i in range(n):
#     num = int(input())
#     arr.append(num)
# sign = []
# for i in range(len(arr)):
#     if i == 0:
#         for j in range(1, arr[i]+1):
#             sign.append("+")
#             stack.append(j)
#         input_num = arr[i]
#         check[stack.pop()] = True
#         sign.append("-")
#     elif input_num > arr[i]:
#         for j in range(input_num-1, arr[i]-1, -1):
#             check[stack.pop()] = True
#             sign.append("-")
#     elif input_num < arr[i]:
#         for j in range(input_num+1, arr[i]+1):
#             stack.append(j)
#             sign.append("+")
#         input_num = arr[i]
#         check[stack.pop()] = True
#         sign.append("-")
    
        
            
        
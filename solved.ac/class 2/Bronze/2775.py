# 2775번 부녀회장이 될테야
# 동적계획법 - Top-Down 방식
T = int(input())
init_num = 0
init_list = []
list_memo = []
for i in range(1, 15):
    init_num += i
    init_list.append(init_num)

def apt(k, n, memo):
    if n == 1:
        return 1
    elif k == 1:
        return init_list[n-1]
    else:
        if memo[k][n] > 0 :
            return memo[k][n]
        
        memo[k][n] = apt(k, n-1, memo) + apt(k-1, n, memo)

        return memo[k][n]
    
for test in range(T):
    k = int(input())
    n = int(input())
    for i in range(k+1):
        list_memo.append([])
        for j in range(n+1):
            list_memo[i].append(0)

    print(apt(k, n, list_memo))


# T = int(input())
# init_num = 0
# init_list = []
# for i in range(1, 15):
#     init_num += i
#     init_list.append(init_num)

# def apt(k, n):
#     if k == 1:
#         return init_list[n-1]
#     else:
#         sum = 0
#         for i in range(1, n+1):
#             sum += apt(k-1, i)

#         return sum
    
# while True:
#     k = int(input())
#     n = int(input())
#     print(apt(k, n))


# 시간초과
# T = int(input())

# def apt(k, n):
#     p_list = []
#     r_list = []
#     if k == 0:
#         for i in range(1, n+1):
#             p_list.append(i)
#         return p_list[n-1]
#     else:
#         sum = 0
#         for i in range(1, n+1):
#             sum += apt(k-1, i)
#             r_list.append(sum)
#         return r_list[n-1]
    
# while True:
#     k = int(input())
#     n = int(input())
#     print(apt(k, n))


    
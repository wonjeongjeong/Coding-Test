# 18110번 solved.ac
# 내장된 round 함수는 사사오입 원칙을 따른다.
import sys
input = sys.stdin.readline

def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
n = int(input())
if n == 0:
    print(0)
else:
    opinion = []
    ex = custom_round(n * 15 / 100)
    for i in range(n):
        level = int(input())
        opinion.append(level)
        
    opinion.sort()
    opinion = opinion[ex:n-ex]

    average = sum(opinion) / len(opinion)
    print(custom_round(average))

# 틀렸습니다
# n = int(input())
# if n == 0:
#     print(0)
# else:
#     opinion = []
#     ex = round(n * 15 / 100)
#     for i in range(n):
#         level = int(input())
#         opinion.append(level)
        
#     opinion.sort()
#     opinion = opinion[ex:n-ex]

#     average = sum(opinion) / len(opinion)
#     if round(average) < 1:
#         print(1)
#     elif round(average) > 30:
#         print(30)
#     else:
#         print(round(average))

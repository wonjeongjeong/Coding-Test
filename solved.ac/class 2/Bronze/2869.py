# 2869번 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())

day = (V-B) // (A-B)
etc = (V-B) % (A-B)
if etc == 0:
    print(day)
else:
    print(day + 1)

# A, B, V = map(int, input().split())
# meter = 0
# day = 0
# while True:
#     day += 1
#     meter += A
#     if meter >= V:
#         break
#     meter -= B
# print(day)
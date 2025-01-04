# 4153번 직각삼각형
while True:
    length = list(map(int, input().split()))
    if length == [0, 0, 0]:
        break
    length.sort()
    a = length[0]
    b = length[1]
    c = length[2]

    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")
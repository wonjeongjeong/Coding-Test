# 2884번 알람 시계
h, m = map(int, input().split())

if m >= 45:
    change_m = m - 45
    print(f"{h} {change_m}")
else:
    change_m = 60 - (45- m)
    if h == 0:
        change_h = 23
    else:
        change_h = h - 1
    print(f"{change_h} {change_m}")
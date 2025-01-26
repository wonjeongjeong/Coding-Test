# 17626번 Four Squares
# 다시 풀어볼 것 !!
N = int(input())

square = [0 if i**0.5 % 1 != 0 else 1 for i in range(N+1)]

count = 4
for i in range(int(N**0.5), 0, -1):
    if square[N] == 1:
        count = 1
        break
    elif square[N-i**2] == 1:
        count = 2
        break
    else:
        for j in range(int((N-i**2)**0.5), 0, -1):
            if square[(N-i**2)-j**2] == 1:
                count = 3
print(count)
# 10814번 나이순 정렬
# sort key로 해결
N = int(input())
user_list = []

for i in range(N):
    user = list(map(str, input().split()))
    user[0] = int(user[0])
    user_list.append(user)

user_list = sorted(user_list, key = lambda x: x[0])

for i in range(N):
    print(f"{user_list[i][0]} {user_list[i][1]}")
# 17219번 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
address = {}

for i in range(N):
    email, password = map(str, input().strip().split())
    address[email] = password
    
for i in range(M):  
    site = input().strip()
    print(address[site])

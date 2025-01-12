# 1920번 수 찾기
# 이진 탐색

N = int(input())
A = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

A.sort()

for num in m_list:
    start = 0
    end = N-1
    found = 0
    
    while start <= end:
        mid = (start+end)//2
        
        if A[mid] == num:
            found = 1
            break
        
        elif A[mid] < num:
            start = mid + 1
            
        else:
            end = mid - 1
            
    print(found)
        
# 선형탐색으로 인한 시간 초과
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# m_list = list(map(int, input().split()))

# for i in range(M):
#     if m_list[i] in A:
#         print(1)
#     else:
#         print(0)
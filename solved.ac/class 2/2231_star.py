# 2231번 분해합
# 북마크 => 다시 풀어보기 (시간복잡도 줄여보자 !)
N = input()
result = False

for num in range(1, int(N)):
    str_num = str(num)
    number = [str_num[i] for i in range(len(str_num))]

    index_sum = 0
    for j in range(len(str_num)):
        index_sum += int(number[j])
    
    if int(N) == num + index_sum:
        print(num)
        result = True
        break
    
if result == False:
    print("0")
    
    
# 나눗셈 이용한 정은님 코드
def calc(N):
    start = max(1, N - len(str(N)) * 9)
    for M in range(start, N):
        sum = M
        temp = M
        while temp > 0:
            sum += temp % 10
            temp //= 10
        if sum == N:
            return M
    return 0

N = int(input())
print(calc(N))
        





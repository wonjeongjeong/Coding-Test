# 1541번 잃어버린 괄호
# 그리디 알고리즘
equation = input()

# '-' 기준으로 나누기
parts = equation.split('-')

# 첫 번째 파트는 무조건 더하기
initial_sum = sum(map(int, parts[0].split('+')))

# 나머지 파트는 각각 내부 값을 더한 뒤 빼기
remaining_sum = 0
for part in parts[1:]:
    remaining_sum += sum(map(int, part.split('+')))

# 결과 계산
result = initial_sum - remaining_sum
print(result)

# 틀렸습니다
# equation = input()
# num = equation[0]
# arr = []
# symbol = []

# for i in range(1, len(equation)):
#     if num == 'x':
#         num = equation[i]
#         continue

#     try:
#         e = int(equation[i])
#         num = num + equation[i]
        
#     except:
#         symbol.append(equation[i])
#         num = int(num)
#         arr.append(num)
#         num = 'x'
        
#     if i == len(equation) - 1:
#         num = int(num)
#         arr.append(num)

# result = arr[0]
# is_minus = False

# for i in range(len(symbol)):
#     if symbol[i] == '-':
#         is_minus = True
#     else:
#         is_minus = False
        
#     if is_minus:
#         result -= arr[i+1]
#     else:
#         result += arr[i+1]
        
# print(result)
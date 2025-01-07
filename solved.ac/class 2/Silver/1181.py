# 1181번 단어 정렬
N = int(input())
word_list = [0] * 51
word_count = [0] * 51
for i in range(1, N+1):
    word = input()
    length = len(word)
    if word_count[length] == 0:
        new_list = [word]
        word_list[length] = new_list
        word_count[length] += 1
    else:
        old_list = word_list[length]
        if word in old_list:
            continue
        old_list.append(word)
        word_count[length] += 1

for i in range(1, 51):
    if word_list[i] != 0:
        if len(word_list[i]) > 1:
            sort_list = sorted(word_list[i])
            word_list[i] = sort_list
        for j in range(len(word_list[i])):
            print(word_list[i][j])

# 시간초과
# N = int(input())
# word_list = []
# word_count = [0] * 20001
# sum = 0
# def index(len):
#     result = 0
#     for i in range(len+1):
#         if word_count[i] != 0:
#             result += word_count[i]
#     return result

# for i in range(N):
#     word = input()
#     length = len(word)
#     insert = False
#     if i == 0:
#         word_list.append(word)
#         word_count[length] += 1
#     else:
#         if word_count[length] == 0:
#             for j in range(len(word_list)):
#                 if len(word_list[j]) > len(word):
#                     word_list.insert(j, word)
#                     word_count[length] += 1
#                     insert = True
#                     break
#             if insert == False:
#                 word_list.append(word)
#                 word_count[length] += 1
#         else:
#             sum = index(length)
#             if word in word_list:
#                 continue
#             for j in range(word_count[length]):
#                 if word_list[sum-1-j] < word:
#                     word_list.insert(sum-j, word)
#                     word_count[length] += 1
#                     insert = True
#                     break
#             if insert == False:
#                 word_list.insert(sum-word_count[length], word)
#                 word_count[length] += 1
            
# for i in range(len(word_list)):
#     print(word_list[i])
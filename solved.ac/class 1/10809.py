# 10809번 알파벳 찾기
S = input()

alphabet = [-1 for _ in range(26)]

for i in range(len(S)):
    word_index = ord(f"{S[i]}") - ord("a")
    if alphabet[word_index] == -1:
        alphabet[word_index] = i
    else:
        pass
    
for i in range(26):
    if i == 25:
        print(alphabet[i],end="")
    else:
        print(f"{alphabet[i]} ",end="")
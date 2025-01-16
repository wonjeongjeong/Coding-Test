# 1620번 나는야 포켓몬 마스터 이다솜
# 딕셔너리 사용
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_to_num = {}
num_to_pokemon = {}

for i in range(1, N+1):
    name = input().strip()
    pokemon_to_num[name] = i
    num_to_pokemon[i] = name

for i in range(M):
    quest = input().strip()
    if quest.isdigit():  # 숫자인 경우
        print(num_to_pokemon[int(quest)])
    else:
        print(pokemon_to_num[quest])
        
# 시간 초과과
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# pokemon = [0]
# for i in range(N):
#     name = input().strip()
#     pokemon.append(name)

# for i in range(M):
#     quest = input().strip()
#     try:
#         quest_n = int(quest)
#         print(pokemon[quest_n])
#     except:
#         quest_a = quest
#         print(pokemon.index(quest_a))
    
    
    
    
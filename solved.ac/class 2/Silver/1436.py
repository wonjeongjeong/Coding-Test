# 1436번 영화감독 숌
# 브루트포스 알고리즘

end_num = "666"
N = int(input())
series = 665
count = 0
while True:
    if count == N:
        break
    series += 1
    if end_num in str(series):
        count += 1
    
print(series)
        
    
        


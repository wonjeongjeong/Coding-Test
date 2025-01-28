# 2525번 오븐시계
H, M = map(int, input().split())
C = int(input())

end_minute = M + C

if end_minute >= 60:
    result_m = end_minute % 60
    result_h = H + end_minute // 60
    if result_h > 23:
        result_h = result_h - 24
else:
    result_m = end_minute
    result_h = H        
    
print(f"{result_h} {result_m}")
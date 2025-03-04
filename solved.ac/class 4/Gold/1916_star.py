# 1916번 최소비용 구하기
import sys
import heapq 

input = sys.stdin.readline

N = int(input())
M = int(input())

total_cost = [[] for _ in range(N+1)]
    
for i in range(M):
    start, arrive, cost = map(int, input().split())
    total_cost[start].append([arrive, cost])

q_start, q_arrive = map(int, input().split())
costs = [1e9 for _ in range(N+1)]
heap = []
costs[q_start] = 0
heapq.heappush(heap, [0, q_start])

while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_cost:
        continue
    for next_v, next_cost in total_cost[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue
        
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
        
print(costs[q_arrive])

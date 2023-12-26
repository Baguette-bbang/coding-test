from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def elevator_bfs(F, S, G, U, D):
    visited = [False for _ in range(F+1)]
    queue = deque([(S,0)])
    visited[S] = True
    while queue:
        floor, cost = queue.popleft()
        
        if floor == G:
            return cost
        
        new_floors = [floor+U, floor-D]
        for new_floor in new_floors:
            if 0 < new_floor <= F and not visited[new_floor]:
                 queue.append((new_floor, cost+1))
                 visited[new_floor] = True
    return -1
# 엘레베이터를 쓸 수 없는 조건은?
# 도착하려는 층보다 높은데 내려갈 수 없을 때
# 도착하려는 층보다 낮은데 올라갈 수 없을 때
# 아다구가 안맞을경우.. 이건 뭐지
if (S < G and U ==0) or (S > G and D == 0):
    print('use the stairs')
else:
    cost = elevator_bfs(F,S,G,U,D)
    if cost == -1:
        print('use the stairs')
    else:
        print(cost)
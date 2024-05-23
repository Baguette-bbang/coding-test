from collections import deque
# bfs로 접근
# 1. 최댓값과 최솟값 구하기
# 2. 강수 높이 설정 반복은 최솟값~최댓값-1
# 3. 강수 높이 이하인 것들은 잠기게 하기
# 4. 잠기지 않은 안전영역의 개수 구하기 bfs로 탐색

# 조건1. 매 반복마다 딥카피를 사용하면 시간제한에 걸릴 듯 함.

n = int(input())

graph = []
min_val = float('inf')
max_val = 0
for _ in range(n):
    line = list(map(int, input().split()))
    min_val = min(min(line), min_val)
    max_val = max(max(line), max_val)
    graph.append(line)

# print(graph)
# print(min_val, max_val)
moves = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(i, j, visited):
    queue = deque([(i,j)])
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
def drown(height, visited):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                visited[i][j] = True

# print(visited_or_drown)
max_safe_area = 0
for height in range(min_val, max_val):
    # 초기화
    visited_or_drown = [[False] * n for _ in range(n)]

    drown(height, visited_or_drown)
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if not visited_or_drown[i][j]:
                safe_area += 1
                bfs(i, j, visited_or_drown)
    max_safe_area = max(max_safe_area, safe_area)
print(max(max_safe_area, 1))
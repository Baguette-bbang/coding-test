from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

def safety_bfs(height, N, graph, visited, start):
    x, y = start
    queue = deque([(x,y)])
    visited[x][y] = True
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        x, y = queue.popleft()
        for add_x, add_y in moves:
            new_x = add_x+x
            new_y = add_y+y
            if (0<=new_x<N)and (0<=new_y<N) and graph[new_x][new_y] > height and not visited[new_x][new_y]:
                queue.append((new_x,new_y))
                visited[new_x][new_y] = True

max_value = max(max(row) for row in graph) + 1
min_value = min(min(row) for row in graph)

answer = 1
for height in range(min_value, max_value):
    safety_zone = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and not visited[i][j]:
                safety_bfs(height, N, graph, visited, (i,j))
                safety_zone += 1
    if safety_zone > answer:
        answer = safety_zone

print(answer)
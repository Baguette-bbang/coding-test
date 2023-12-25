from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
        
# def make_move_list(location, visited, graph, N, M):
#     move = [(0,1,1),(1,0,1),(0,-1,1),(-1,0,1)]
#     move_list = []
#     temp_list = []
    
#     for i in move:
#         temp_list.append(tuple(map(sum, zip(i, location))))
        
#     for i in temp_list:
#         x = i[0]
#         y = i[1]
#         if 0 <= x < N and 0 <= y < M and not visited[x][y] and graph[x][y] == 1:
#             move_list.append(i)
            
#     return move_list

visited = [[False for _ in range(M)]for _ in range(N)]
def bfs(visited, graph):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 이동 가능한 네 방향
    # i, j, cost
    queue = deque([(0,0,0)])
    visited[0][0] = True
    while queue:
        print(queue)
        x, y, cost = queue.popleft()
        if x == N - 1 and y == M - 1:
            return cost  # 도착 지점에 도달했을 때 비용 반환
        
        for add_x, add_y in moves:
            new_x, new_y = x+add_x, y+add_y
            if 0 <= new_x < N and 0 <= new_y < M and not visited[new_x][new_y] and graph[new_x][new_y] == 1:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, cost + 1))
    return 0

cost = bfs(visited, graph)
print(cost+1)
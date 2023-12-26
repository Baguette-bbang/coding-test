from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def complex_bfs(graph, visited, start, n):
    x, y = start
    queue = deque([(x,y)])
    visited[x][y] = True
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    cost = 1
    while queue:
        x, y = queue.popleft()
        for add_x, add_y in moves:
            new_x = add_x + x
            new_y = add_y + y
            if 0<=new_x<n and 0<=new_y<n and not visited[new_x][new_y] and graph[new_x][new_y]==1:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                cost += 1
    return cost

complex_num = 0
each_complex = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cost = complex_bfs(graph, visited, (i,j), n)
            each_complex.append(cost)
            complex_num+=1

each_complex.sort()
print(complex_num)
for complex in each_complex:
    print(complex)
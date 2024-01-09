# 점을 입력받고 해당 점을 통해 만들어질 수 있는 테트로미노 중 가장 최대값을 찾기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
##### 1차 풀이(시간초과) #####
def make_other(start, m, n, cnt, value, graph, visited):
    if cnt == 4:
        return value

    max_value = 0
    x, y = start
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            max_value = max(max_value, make_other((nx, ny), m, n, cnt + 1, value + graph[nx][ny], graph, visited))
            visited[nx][ny] = False
        else:
            break
    return max_value
# 예외처리 ㅗ 도형은 따로 탐색하는 로직을 만들어야함.
# 한점에서 시작하여 좌측, 우측, 상단, 하단의 세 점을 방문해야한다.
def make_ㅗ(start, m, n, graph):
    max_value = 0
    x, y = start
    # 상하우좌
    moves = [[(0,-1),(-1,-1),(1,-1)],[(0,1),(-1,1),(1,1)],[(1,0),(1,-1),(1,1)],[(-1,0),(-1,-1),(-1,1)]]
    # 시작점에서부터 ㅗ도형을 방향전환하며 그리기
    for move in moves:
        value = graph[x][y]
        for dx,dy in move:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                value += graph[nx][ny]
            else:
                break
        max_value = max(max_value, value)
    return max_value
# 각 점에 해당되는 최대값중 가장 최대값을 찾기
max_value = 0
for i in range(n):
    for j in range(m):
        # start는 방문하고 시작해야함.
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True
        max_value =  max(max_value,make_other((i,j), m, n, 1, graph[i][j], graph, visited),make_ㅗ((i,j), m, n, graph))
print(max_value)

##### 2차 풀이(성공) #####
def calculate_tetris(x, y, n, m, graph, moves):
    max_value = 0
    for move in moves:
        value = 0
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                value += graph[nx][ny]
            else:
                break
        else:
            max_value = max(max_value, value)
    return max_value

def make_tetris(n, m, graph):
    moves=[[(0,0),(0,1),(0,2),(0,3)],\
        [(0,0),(1,0),(2,0),(3,0)],\
        [(0,0),(1,0),(0,1),(1,1)],\
        [(0,0),(1,0),(2,0),(2,1)],\
        [(0,1),(1,1),(2,1),(2,0)],\
        [(0,0),(0,1),(1,1),(2,1)],\
        [(0,0),(0,1),(1,0),(2,0)],\
        [(0,0),(1,0),(1,1),(1,2)],\
        [(0,2),(1,1),(1,2),(1,0)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,1),(1,1),(1,0),(2,0)],\
        [(1,0),(1,1),(0,1),(0,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,1),(1,0),(1,1),(1,2)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,1),(1,1),(1,0),(2,1)]]

    max_value = 0
    
    for i in range(n):
        for j in range(m):
            max_value = max(max_value, calculate_tetris(i, j, n, m, graph, moves))
    return max_value

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
print(make_tetris(n, m, graph))
# 백준 2583 영역 구하기 실버 1
# 시작 19시 3분
# 종료 19시 34분

# 1. 직사각형이 있는 칸을 모두 칠하기
# 2. 직사각형이 존재하지 않는 곳 구하기
# 3. 각 직사각형의 범위 dfs로 체크하기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 입력받기
m, n, k = map(int, input().split())
input_squares = []
for _ in range(k):
    input_squares.append(list(map(int, input().split())))

# 입력 맵 만들기
graph = [[False] * n for _ in range(m)]

# 1. 직사각형이 있는 칸을 모두 칠하기
for sx, sy, ex, ey in input_squares:
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = True
            
moves = [(0,1), (1,0), (-1,0), (0,-1)]
def dfs(x, y, count):
    graph[y][x] = True # 방문처리
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not graph[ny][nx]:
            count = dfs(nx, ny, count+1)
    return count
        
sections = []
for y in range(m):
    for x in range(n):
        if not graph[y][x]: # 2. 직사각형이 존재하지 않는 곳 구하기
            # 3. 각 직사각형의 범위 dfs로 체크하기
            sections.append(dfs(x,y,1))

print(len(sections))
print(*sorted(sections))
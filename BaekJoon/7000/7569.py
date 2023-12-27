import sys
from collections import deque
input = sys.stdin.readline
# 입력 : M상자열의수, N상자행의수, H상자의수
m,n,h = map(int, input().split())
start_tomatos = []
# 3차원 배열 초기화
graph = [[[0 for _ in range(m)]for _ in range(n)] for _ in range(h)]
count_0 = 0
for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))
        # 시작 토마토(이미 익은 토마토 1)위치 넣기
        start_tomatos.extend([(i,j,index,0) for index, value in enumerate(graph[i][j]) if value == 1])
        # 입력 받은 배열의 0의 개수 세기
        count_0 += graph[i][j].count(0)
        
def tomato_bfs(graph, start, m,n,h):
    # start : 큐에 모든 1인 토마토를 넣은 리스트
    queue = deque(start)
    # 움직이는 방향 6개 위, 아래, 좌, 우, 상, 하
    moves = [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
    temp = []
    while queue:
        z,y,x, cost = queue.popleft()
        for dz,dy,dx in moves:
            nz,ny,nx = z+dz, y+dy, x+dx
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and graph[nz][ny][nx]==0:
                queue.append((nz,ny,nx,cost+1))
                graph[nz][ny][nx] = 1
                # 다 익기까지의 날짜를 세기 위한 용도(약간 비효율적임)
                temp.append(cost+1) 
    # 모든 면 방문
    for plane in graph:
        # 모든 행 방문
        for row in plane:
            # bfs로 모든 경로를 탐색했음에도 익지 않은 토마토가 있을경우
            if 0 in row:
                return -1
    return temp[-1]
# 0이 없다면(이미 다 익은 토마토라면) 0출력
if count_0 == 0:
    print(0)
# 다 익지 못하는 토마토가 있거나 다 익기까지의 날짜 (-1 or days)출력
else:
    print(tomato_bfs(graph, start_tomatos, m,n,h))
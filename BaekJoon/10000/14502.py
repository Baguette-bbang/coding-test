from itertools import combinations
from collections import deque
from copy import deepcopy
# 0은 빈 칸, 1은 벽 2는 바이러스
# 연구소의 지도가 주어졌을 경우 
# 벽을 세 개 세운 후 가장 큰 안전영역을 구하여라

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
# 특정 0을 세 개를 중복되지 않게 뽑아야 한다. 몇 가지 경우의 수가 나오며,


zero_area = []
virus = deque()
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            zero_area.append((i,j))
        if map[i][j] == 2: 
            virus.append((i,j))
make_wall = list(combinations(zero_area,3))

# 바이러스를 퍼뜨려야한다.
max_safety = 0

for walls in make_wall: 
    # 벽을 뽑고 벽을 세워야함.
    temp_map = deepcopy(map)
    for wall in walls:
        temp_map[wall[0]][wall[1]] = 1
    # 새로 벽을 세웠으니 바이러스를 퍼뜨려야함. bfs
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    temp_virus = deepcopy(virus)
    while temp_virus:
        x,y = temp_virus.popleft()
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and temp_map[nx][ny]==0:
                temp_map[nx][ny] = 2
                temp_virus.append((nx,ny))
    cnt = 0
    # 청정지역을 찾아야함.
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                cnt +=1
    # 최대 안전구역 크기를 구해야함.
    max_safety = max(max_safety, cnt)
print(max_safety)

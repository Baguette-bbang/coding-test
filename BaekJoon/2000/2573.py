# 2차원 배열에 표시
# 빙산의 높이는 1~10이다.
# 바다는 0으로 표시된다.
# 1년마다 빙산의 높이는 1 감소한다.
# 한 덩어리의 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하여라
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않는다면 0을 출력

# 1. 빙산의 높이를 1씩 낮춘다.
# 2. 빙산이 몇 덩어리가 되었는지 체크한다.
from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
arctic = list(list(map(int, input().split())) for _ in range(n))
moves = [[0,1], [1,0], [-1,0], [0,-1]]

def iceberg_melt():
    global arctic
    melting = []  # 빙산이 녹을 위치와 녹는 양을 저장

    for i in range(n):
        for j in range(m):
            if arctic[i][j] > 0:
                sea_count = 0
                for dr, dc in moves:
                    nr, nc = dr + i, dc + j
                    if 0 <= nr < n and 0 <= nc < m and arctic[nr][nc] == 0:
                        sea_count += 1
                if sea_count > 0:
                    melting.append((i, j, sea_count))

    # 녹는 위치 업데이트
    for i, j, sea_count in melting:
        arctic[i][j] = max(arctic[i][j] - sea_count, 0)

    # 남아있는 빙산 위치 반환
    return [(i, j) for i in range(n) for j in range(m) if arctic[i][j] > 0]

def bfs(point):
    queue = deque()
    queue.append(point)
    while queue:
        r, c = queue.popleft()
        for dr, dc in moves:
            nr, nc = dr+r, dc+c
            if 0<=nr<n and 0<=nc<m and arctic[nr][nc] > 0 and not visited[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = True
    return 1

iceberg = [] # 빙산의 위치정보가 담긴 리스트
for i in range(n):
    for j in range(m):
        if arctic[i][j] > 0:
            iceberg.append((i,j))
            
answer = 0 # 빙산이 두덩어리 이상이 되는 시간
flag = False
while iceberg:
    visited = list(list(False for _ in range(m)) for _ in range(n))
    
    # 빙산 덩어리의 수
    cnt = 0 
    # 빙산 덩어리 개수 세기
    for i in range(len(iceberg)):
        if not visited[iceberg[i][0]][iceberg[i][1]]:
            cnt += bfs(iceberg[i])
        
    if cnt > 1:
        flag = True
        break
    
    # 1년마다 빙산의 높이는 1씩 감소
    answer += 1
    iceberg = iceberg_melt()
if flag:
    print(answer)
else:
    print(0)
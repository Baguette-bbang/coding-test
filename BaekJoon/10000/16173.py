# 16173번 점프왕 쩰리 - 실버4 문제
# 6시 43분 시작
# 0,0 위치에서 출발
# 오른쪽과 아래로만 이동가능
# 자신이 있는 칸의 숫자만큼 이동 가능
# 숫자로 인해 사각형을 넘어갈 시 패배

# 1. bfs로 탐색
# 2. 종료 지점인가?
# 3. 방문 했는지, 범위 안인지, 확인
from collections import deque
n = int(input())
queue = deque()
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
queue.append((0,0))
visited = [[False]*n for _ in range(n)]
moves = [(0,1), (1,0)]
visited[0][0] = True
while queue:
    x, y = queue.popleft()
    if graph[x][y] == -1:
        print('HaruHaru')
        break
    for dx, dy in moves:
        nx, ny = x + dx*graph[x][y], y + dy*graph[x][y]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            queue.append((nx,ny))
            visited[nx][ny] = True
else:
    print('Hing')
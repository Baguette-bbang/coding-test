#     # 상, 하, 좌, 우 
#     # G가 목표지점, R은 시작지점
#     # R로 갈 수 없다면 -1
#     # 게임판 위의 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하는 것을 한 번의 이동으로 친다.
#     # 1. 출발점, 도착점 위치 찾기
#     # 2. 출발점 기준으로 BFS

from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    start = []
    end = []
    
    # 출발점과 도착점 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                end = (i, j)
    
    # 방문 체크 및 BFS 초기화
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        r, c, dist = queue.popleft()
        if r == end[0] and c == end[1]:
            return dist
        for dr, dc in moves:
            nr = r
            nc = c
            while True:
                next_r = nr + dr
                next_c = nc + dc
                if 0<=next_r<n and 0<=next_c<m and board[next_r][next_c] != 'D':
                    nr, nc  = next_r, next_c
                else:
                    break
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr,nc, dist+1))
    return -1
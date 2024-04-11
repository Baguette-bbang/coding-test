from collections import deque

def solution(maps):
    # BFS 함수 정의
    def bfs(start, target):
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque([(start, 0)])
        visited[start[0]][start[1]] = True

        while queue:
            (r, c), dist = queue.popleft()
            if maps[r][c] == target:
                return dist

            for dr, dc in moves:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    queue.append(((nr, nc), dist + 1))

        return -1

    # 시작점, 레버, 출구 위치 찾기
    start = lever = exit = None
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # 출발점에서 레버까지의 최단 경로 찾기
    to_lever = bfs(start, 'L')
    if to_lever == -1:
        return -1

    # 레버에서 출구까지의 최단 경로 찾기
    to_exit = bfs(lever, 'E')
    if to_exit == -1:
        return -1

    return to_lever + to_exit

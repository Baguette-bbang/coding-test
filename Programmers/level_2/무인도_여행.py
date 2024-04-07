from collections import deque
def solution(maps):
    answer = []
    # 1x1 크기의 사각형들로 이루어진 직사각형 격자 형태
    # 격자의 각 칸에는 'X' 또는 1~9 사이의 자연수가 적혀있다.
    
    # 1. split 처리
    # 2. X가 아닌 위치 파악
    # 3. BFS 돌면서 visited 업데이트 및 섬의 기간 구하기
    
    r_length = len(maps)
    c_length = len(maps[0])
    island_locations = []
    
    # 1. 한 문자열을 문자로 나누기
    for i in range(len(maps)):        
        maps[i] = list(maps[i])
        for j in range(len(maps[i])):
            # 2. X아닌 것의 위치 파악
            if maps[i][j] != 'X':
                island_locations.append([i,j])
    
    # 3. BFS 처리하기
    visited = [[False] * c_length for _ in range(r_length)]
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    def bfs(start):
        queue = deque()
        queue.append(start)
        date = int(maps[start[0]][start[1]])
        visited[start[0]][start[1]] = True
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in moves:
                nr, nc = r+dr, c+dc
                if 0 <= nr < r_length and 0 <= nc < c_length and not visited[nr][nc] and maps[nr][nc] != 'X':
                    queue.append([nr,nc])
                    visited[nr][nc] = True
                    date += int(maps[nr][nc])
        return date
    
    for r, c in island_locations:
        if not visited[r][c]:
            answer.append(bfs([r,c]))
    answer.sort()
    if not answer:
        answer = [-1]
    return answer
from collections import deque
def bfs(visited, maps, r, c):
    queue = deque([(0,0,0)])
    visited[0][0] = True
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    while queue:
        temp_r, temp_c, cost = queue.popleft()
        if temp_r == r-1 and temp_c == c-1:
            return cost+1
        for add_r, add_c in moves:
            new_r = temp_r + add_r
            new_c = temp_c + add_c
            if 0<=new_r< r and 0<=new_c<c and maps[new_r][new_c]==1 and not visited[new_r][new_c]:
                queue.append((new_r, new_c, cost+1))
                visited[new_r][new_c] = True
    return -1

def solution(maps):
    answer = 0
    r = len(maps)
    c = len(maps[0])
    visited = [[False]*c for _ in range(r)]
    answer = bfs(visited, maps, r, c)
    return answer
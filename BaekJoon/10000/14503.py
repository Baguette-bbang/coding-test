n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

def can_clean(cleaned, maps, r, c, d, n, m):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

    for _ in range(4):
        d = (d - 1) % 4  # 왼쪽으로 회전
        new_r, new_c = r + moves[d][0], c + moves[d][1]
    
        if 0 <= new_r < n and 0 <= new_c < m and maps[new_r][new_c] == 0 and not cleaned[new_r][new_c]:
            return new_r, new_c, d
    return -1

def robot_dfs(cleaned, maps, r, c, d, n, m):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
    answer = 0
    # 반시계 회전
    while(1):
        # 현재 칸이 아직 청소되지 않았다면 현재 칸을 청소한다.
        if not cleaned[r][c]:
            cleaned[r][c] = True
            answer += 1
        # 반시계방향 회전
        # 주변 4칸 중 청소가능한 칸이 있는가?
        next_step = can_clean(cleaned, maps, r, c, d, n, m)
        # 주변 4칸 중 청소가능한 칸이 있는 경우
        if next_step != -1:
            r, c, d = next_step
        else:
            # 주변 4칸 중 청소가능한 칸이 없는 경우
            back_d = (d + 2) % 4
            back_r, back_c = r + moves[back_d][0], c + moves[back_d][1]
            # 바라보는 방향 그대로 후진 
            if 0 <= back_r < n and 0 <= back_c < m and maps[back_r][back_c] != 1:
                r, c = back_r, back_c
            else:
                break
    return answer

cleaned = [[False]*m for _ in range(n)]
print(robot_dfs(cleaned, maps, r, c, d, n, m))

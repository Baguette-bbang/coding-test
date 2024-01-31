from collections import deque
import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
room_info = [list(map(int, input().split())) for _ in range(r)]

def cal_dust(cur_dust, spread_dir):
    spread_dust = cur_dust // 5
    remain_dust = cur_dust - spread_dust * spread_dir
    return remain_dust, spread_dust

def check_loc(room_info, i, j, r, c):
    return 0 <= i < r and 0 <= j < c and room_info[i][j] != -1

def spread_dust_in_room(room_info, r, c):
    queue = deque()
    temp_room = [[0] * c for _ in range(r)]

    # 미세먼지 위치 정보 확인
    for i in range(r):
        for j in range(c):
            if room_info[i][j] > 0:
                queue.append((i, j, room_info[i][j]))

    # 미세먼지 확산 처리
    while queue:
        x, y, dust = queue.popleft()
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        dir_cnt = 0
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if check_loc(room_info, nx, ny, r, c):
                dir_cnt += 1

        remain_dust, spread_dust = cal_dust(dust, dir_cnt)
        temp_room[x][y] += remain_dust
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if check_loc(room_info, nx, ny, r, c):
                temp_room[nx][ny] += spread_dust

    # 미세먼지 업데이트
    for i in range(r):
        for j in range(c):
            if room_info[i][j] != -1:
                room_info[i][j] = temp_room[i][j]

def find_air_cleaner(room_info):
    for i in range(len(room_info)):
        if room_info[i][0] == -1:
            return i

def move_dust(room_info, x, r, c):
    # 공기청정기 위치를 기준으로 상단 부분과 하단 부분으로 나눔
    upper_cleaner, lower_cleaner = x, x + 1

    # 덮어씌워도 상관없다. 값이 밀리면서 채워지기에 그렇다.
    # 상단 공기 순환 (반시계 방향)
    # 좌측 열
    for i in range(upper_cleaner-1, 0, -1):
        room_info[i][0] = room_info[i-1][0]
    # 상측 행
    for j in range(c-1):
        room_info[0][j] = room_info[0][j+1]
    # 우측 열
    for i in range(upper_cleaner):
        room_info[i][c-1] = room_info[i+1][c-1]
    # 하측 행
    for j in range(c-1, 1, -1):
        room_info[upper_cleaner][j] = room_info[upper_cleaner][j-1]
    room_info[upper_cleaner][1] = 0  # 공기청정기 옆 먼지 제거

    # 하단 공기 순환 (시계 방향)
    # 좌측 열
    for i in range(lower_cleaner+1, r-1):
        room_info[i][0] = room_info[i+1][0]
    # 하측 행
    for j in range(c-1):
        room_info[r-1][j] = room_info[r-1][j+1]
    # 우측 열
    for i in range(r-2, lower_cleaner-1, -1):
        room_info[i+1][c-1] = room_info[i][c-1]
    # 상측 행
    for j in range(c-1, 1, -1):
        room_info[lower_cleaner][j] = room_info[lower_cleaner][j-1]
    room_info[lower_cleaner][1] = 0  # 공기청정기 옆 먼지 제거
    
for _ in range(t):
    spread_dust_in_room(room_info, r, c)
    move_dust(room_info, find_air_cleaner(room_info), r,c)
    
dust = 2
for room in room_info:
    dust += sum(room)
print(dust)
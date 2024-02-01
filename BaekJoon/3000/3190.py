from collections import deque
import sys
input = sys.stdin.readline
# 19시 50분까지
# 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다
# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 종료조건 : 벽 또는 자기자신의 몸과 부딪혔는가?
# 보드의 상하좌우 끝에 벽이 존재
# 뱀 위치 초기화 : 0,0 
# 뱀 초기 이동 위치 : 오른쪽
# 몸이 늘어나는 방식 : 몸을 늘려 다음칸에 위치
# 사과를 먹는 방식 : 사과는 사라지고 꼬리는 움직이지 않는다
# 사과가 없다면 : 꼬리를 지운다. 앞으로 나아가기에 그렇다.

n = int(input()) # 맵의 크기
k = int(input()) # 사과이 개수
apple_list = [list(map(int,input().split())) for _ in range(k)]
l = int(input())
move_list = [list(input().split()) for _ in range(l)]

snake = deque()
graph =[[0] * n for _ in range(n)]
graph[0][0] = 1
for r, c in apple_list:
    graph[r-1][c-1] = 4
cur_second = 0
head_loc = [0,0]
snake.append(head_loc)
head_dir = 0 # 처음 뱀의 머리 방향 (동쪽임)
dir_dict = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)} # 머리를 오른쪽 회전 시 동남서북 , 머리를 왼쪽으로 회전 시 북서남동임.

eat_apple = False # 사과를 먹는다면 True 처리
check_ok = True # 범위를 벗어나지 않거나 몸에 부딫히지 않는다면 True

def check_move(graph, n, loc):
    r,c = loc[0],loc[1]
    if 0<=r<n and 0<=c<n and graph[r][c] != 1:
        return True
    return False

idx = 0
while check_ok:
    if idx < len(move_list):
        moves = move_list[idx]
        move_second = int(moves[0])
        move_direction = moves[1]
    
    if move_second == cur_second:
        # 회전 처리
        if move_second == cur_second:
            if move_direction == "L": # 왼쪽 회전임.
                # 동 -> 북, 서 -> 남, 북 -> 서, 남 -> 동
                # 머리의 방향을 변경한다.
                head_dir = (head_dir - 1) % 4
        
            else: # 오른쪽 회전임.
                # 동 -> 남, 서 -> 북, 북 -> 동, 남 -> 서
                head_dir = (head_dir + 1) % 4
        idx+=1
        
    # 변경된 방향 또는 원래 방향으로 이동한다.
    head_loc = [head_loc[0] + dir_dict[head_dir][0], head_loc[1] + dir_dict[head_dir][1]]
    if check_move(graph, n, head_loc):
        if graph[head_loc[0]][head_loc[1]] == 4: # 사과가 있었다면 먹었다는 표시한다.(꼬리를 안자름)
            eat_apple = True
        graph[head_loc[0]][head_loc[1]] = 1
        snake.appendleft(head_loc) # 머리를 늘린다. 앞에서 추가함.
    else: # 범위를 벗어나거나 몸에 부딫힘.
        check_ok = False 
        break
    
    # 사과를 먹엇다면 꼬리는 냅두기
    # 안먹었다면 꼬리를 자르기
    if eat_apple:
        eat_apple = False
    else: # 
        tail = snake.pop()
        graph[tail[0]][tail[1]] = 0
    cur_second += 1

print(cur_second+1)
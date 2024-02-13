n, m = map(int, input().split())
board = [list(map(int, input(). split())) for _ in range(n)]
directions = {1:(0,-1), 2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)}

# 이동
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
def move_cloud(d, s):
    dx, dy = directions[d]
    for idx, [cx, cy] in enumerate(clouds):
        nx = (cx + dx*s)%n
        ny = (cy + dy*s)%n
        clouds[idx] = [nx, ny]
        board[nx][ny] += 1
        
# 물복사버그
def water_copy_bug():
    moves = [(1,1),(-1,-1),(1,-1),(-1,1)]
    for cx, cy in clouds:
        for dx, dy in moves:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0:
                board[cx][cy] += 1

# 새로운 구름 생성
def make_new_cloud():
    new_cloud = []
    clouds.sort()
    for i in range(n):
        for j in range(n): # 여기서 시간 최적화 진행함.
            if len(clouds) > 0 and clouds[0][0] == i and clouds[0][1] == j:
                del clouds[0]
                continue
            if board[i][j]>=2:
                new_cloud.append([i,j])
                board[i][j] -= 2
    return new_cloud

for _ in range(m):
    d, s = map(int, input().split())
    move_cloud(d, s)
    water_copy_bug()
    clouds = make_new_cloud()

sum_water = 0
for line in board:
    sum_water+= sum(line)
print(sum_water)
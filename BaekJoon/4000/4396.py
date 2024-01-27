#지뢰가 없는 지점을 건드리면, 
# 그곳의 상하좌우 혹은 대각선으로 인접한 8개의 칸에 
# 지뢰가 몇 개 있는지 알려주는 0과 8 사이의 숫자가 나타난다.
# 일반 리스트를 받는다.
# .은 .으로 냅두고 
# x만 처리해야한다.
# x의 위치를 하나씩 받고
# 해당 x의 상하좌우 대각선을 검사한다.
# 접근 가능한지 체크한다.
# 접근이 가능하다면 상하좌우 대각선에 지뢰가 몇 개있는지 기입한다.
n = int(input())
board = [list(input()) for _ in range(n)]
x_board = [list(input()) for _ in range(n)]

def check_array(i,j,n):
    if 0<=i<n and 0<=j<n:
        return 1
    else :
        return 0

# 지뢰를 찾는다면 모두 지뢰
def find_land_mine(x_board, board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                x_board[i][j] = '*'
for i in range(n):
    for j in range(n):
        if x_board[i][j] == 'x':
            if board[i][j] == '*':
                find_land_mine(x_board,board)
            else:
                cnt = 0
                moves = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
                for di, dj in moves:
                    ni, nj = i+di, j+dj
                    if check_array(ni,nj,n) and board[ni][nj] == '*':
                        cnt+=1
                x_board[i][j] = cnt
        
for line in x_board:
    for square in line:
        print(square, end='')
    print()
def solution(board, h, w):
    answer = 0
    # 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수 4개의 방향
    # 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board
    # 고른 칸의 위치를 나타내는 두 정수 h, w
    # board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    n = len(board)
    def check_move(i,j):
        if 0<=i<n and 0<=j<n:
            return 1
        else:
            return 0
    
    for dx,dy in moves:
        nx, ny = h+dx, w+dy
        if check_move(nx,ny) and board[h][w] == board[nx][ny]:
            answer += 1
    return answer
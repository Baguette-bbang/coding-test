from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
moves = [(0,1),(-1,0),(0,-1),(1,0)]
board = [[False] * 101 for _ in range(101)]
answer = 0

for _ in range(n):
    sj, si, d, g = map(int,input().split())
    queue = deque()
    queue.append((si,sj))
    queue.append((si+moves[d][0],sj+moves[d][1]))
    board[si][sj] = True
    board[si+moves[d][0]][sj+moves[d][1]] = True
    for _ in range(g):
        temp_queue = queue.copy()
        criteria_i, criteria_j = temp_queue.pop() # 기준점을 잡고 해당 기준으로 
        board[criteria_i][criteria_j] = True
        for j in range(len(temp_queue)):
            di, dj = temp_queue.pop()
            ni = criteria_i - (criteria_j - dj)
            nj = criteria_j + (criteria_i - di)
            queue.append((ni, nj))
            board[ni][nj] = True
for i in range(100):
    for j in range(100):
        if board[i][j]:
            if board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
                answer += 1
print(answer)
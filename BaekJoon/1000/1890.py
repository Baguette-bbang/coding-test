n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[0]* (n) for _ in range(n)]
d[0][0] = 1
for i in range(0, n):
    for j in range(0, n):
        if board[i][j] == 0:
            continue
        if i+board[i][j] < n:
            d[i+board[i][j]][j] += d[i][j]
        if j+board[i][j] < n:
            d[i][j+board[i][j]] += d[i][j]
print(d[n-1][n-1])
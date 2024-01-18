n,m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = maze[0][0]
for r in range(1, n):
    dp[r][0] = dp[r-1][0] + maze[r][0]
for c in range(1, m):
    dp[0][c] = dp[0][c-1] + maze[0][c]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + maze[i][j]
print(dp[n-1][m-1])
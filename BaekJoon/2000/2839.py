# 설탕 배달
# 3Kg 봉지, 5Kg 봉지
# 봉지의 최소 개수를 구하시오
# 정확하지 않으면 -1 출력
n = int(input())
dp = [-1] * (5000+1)
# print(dp)

dp[0] = 0
dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1
# dp[6] = d[3]+d[3] = 2 
# dp[7] = -1
# dp[8] = d[3] + dp[5] = 2
# dp[9] = dp[6] + dp[3] = 3
# 3 또는 5를 빼면됨
for i in range(6, n+1):
    min_val = float('inf')
    # 3
    if dp[i-3] != -1:
        min_val = min(min_val, dp[3] + dp[i-3])
    # 5
    if dp[i-5] != -1:
        min_val = min(min_val, dp[5] + dp[i-5])
    if min_val != float('inf'):
        dp[i] = min_val
print(dp[n])
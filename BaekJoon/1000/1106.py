# 필요한 최소의 고객 수, 홍보 가능한 도시의 수
# 홍보 비용, 홍보비용 당 늘어나는 고객의 수

c, n = map(int, input().split()) 
dp = [float('inf')] * (c+101)
dp[0] = 0
ad_cost_custom = []
for _ in range(n):
    ad_cost, ad_custom = map(int, input().split())
    ad_cost_custom.append((ad_cost, ad_custom))

for cost, custom in ad_cost_custom:
    for i in range(custom, c+101):
        dp[i] = min(min(dp[i:]), dp[i-custom] + cost)
    #print(dp)
# dp[i] = 최소i명을 늘리기 위한 최소 비용
# dp[0] = 0 # dp[1] = 1 # dp[2] = 2 # dp[3] = 3 # dp[4] = 4 
# dp[5] = 3 # dp[6] = 4 # dp[7] = 5 # dp[8] = 6 # dp[9] = 6
# dp[10] = 6
print(min(dp[c:]))
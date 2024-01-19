n = int(input())

# 딱봐도 끝나는 숫자가 중요해 보인다.
# 0으로 끝나면 0이나 1이 와도 괜찮고
# 1로 끝나면 무조건 0이 와야 한다.
# 쉽게 접근하자면 각 자리수마다 0과 1의 개수를 세면 된다.
dp = [[0] * 2 for _ in range(n+1)] # 0~n 자릿수
dp[1][1] = 1
# dp[2][0] = 1

for i in range(2, n+1):
    for j in range(2):
        dp[i][0] = dp[i-1][1] + dp[i-1][0]
        dp[i][1] = dp[i-1][0]
print(sum(dp[n]))
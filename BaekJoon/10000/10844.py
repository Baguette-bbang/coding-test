n = int(input())
d = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    d[1][i] = 1
d[1][0] = 0
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j] = d[i-1][j+1] # 0으로 끝나는 것들은 1로 끝나는 전 레벨의 것들의 개수임.
        elif j==9:
            d[i][j] = d[i-1][j-1] # 9으로 끝나는 것들은 8로 끝나는 전 레벨의 것들의 개수임.
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1] # 나머지 숫자는 그 전 레벨의 -1, +1로 끝나는 것들의 개수의 합
print(sum(d[n])%1000000000)
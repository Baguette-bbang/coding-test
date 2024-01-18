n = int(input())
d = [[0]*(10) for _ in range(n+1)]
for i in range(10): 
    d[1][i] = 1 
temp = 1
for i in range(1,n+1):
    d[i][0] = 1
for i in range(2,n+1):
    for j in range(1,10):
        d[i][j] = d[i-1][j] + d[i][j-1]
print(sum(d[n])%10007)
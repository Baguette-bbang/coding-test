# 동전의 종류, 만들어야 하는 가치
n , k = map(int, input().split())
d = [0] * (k+1)
coins = []
for i in range(n):
    coins.append(int(input()))
d[0]=1
for coin in coins:
    for i in range(coin, k+1):
        d[i] += d[i-coin]
print(d[k])
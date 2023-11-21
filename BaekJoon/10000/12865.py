import sys
input = sys.stdin.readline

N, K = map(int, input().split())
DP = [[0]*(K+1) for _ in range(N+1)]
W,V = [0],[0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

for i in range(1,N+1):
    for j in range(1,K+1):
        if j>=W[i]:
            #print(f"i:{i}, j:{j}, V[i]:{V[i]}, W[i]:{W[i]}")
            #print(DP[i-1][j-W[i]]+V[i], DP[i-1][j-1])
            DP[i][j] = max(DP[i-1][j-W[i]]+V[i], DP[i-1][j])
        else :
            DP[i][j] = DP[i-1][j]
print(DP[N][K])
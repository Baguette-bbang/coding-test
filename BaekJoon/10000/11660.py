import sys

def input():
    return sys.stdin.readline()

# input
N, M = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    
# 누적합 2차원 배열 초기화    
cumulativeArr = [[0 for _ in range(N)] for _ in range(N)]

# 누적합 값 대입
cumulativeArr[0][0] = arr[0][0]
for i in range(1, N):
    cumulativeArr[0][i] = arr[0][i] + cumulativeArr[0][i-1]
    cumulativeArr[i][0] = arr[i][0] + cumulativeArr[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        cumulativeArr[i][j] = arr[i][j] - cumulativeArr[i-1][j-1] + cumulativeArr[i-1][j] + cumulativeArr[i][j-1]

# 누적합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
    answer = 0
    if x1==0 and y1 ==0:    
        answer = cumulativeArr[x2][y2]
    else :
        if x1 ==0 :
            answer = cumulativeArr[x2][y2] - cumulativeArr[x2][y1-1]
        elif y1 ==0 :
            answer = cumulativeArr[x2][y2] - cumulativeArr[x1-1][y2]
        else:
            answer = cumulativeArr[x2][y2] - cumulativeArr[x1-1][y2] - cumulativeArr[x2][y1-1] + cumulativeArr[x1-1][y1-1]
    print(answer)
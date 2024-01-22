n = int(input())
# 마지막 요소의 최솟값이 어떤 요소들의 조합으로 이루어져있는가?
# 그 전의 요소의 최솟값의 조합이다.
# 그렇다면 색깔을 고려하는 것은 어떻게 할 것인가? 이게 문제긴 함
rgbs = [list(map(int, input().split())) for _ in range(n)]
# 각가의 인덱스에 자기 인덱스가 아닌 것들 중 가장 작은 값을 선택
for i in range(1,n):
    for j in range(3):
        if j==0:
            rgbs[i][j] += min(rgbs[i-1][j+1], rgbs[i-1][j+2])
        elif j==1:
            rgbs[i][j] += min(rgbs[i-1][j-1], rgbs[i-1][j+1])
        else:
            rgbs[i][j] += min(rgbs[i-1][j-1], rgbs[i-1][j-2])
print(min(rgbs[-1]))
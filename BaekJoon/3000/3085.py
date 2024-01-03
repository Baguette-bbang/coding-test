# 사탕의 색이 다른 인접한 두 칸을 골라야한다.
# 고른 칸에 들어있는 사탕을 서로 교환한다.
# 모두 같은 색인 가장 긴 행 또는 열을 고른 다음 모두 먹는다.
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
# 먹을 수 있는 사탕의 최대 개수는?
n = int(input()) # 보드의 크기
candies = [list(input()) for _ in range(n)]

def find_candy_num(candies):
    max_candy = 0

    # 행 탐색
    for i in range(n):
        count = 1
        for j in range(1, n):
            if candies[i][j] == candies[i][j-1]:
                count += 1
                max_candy = max(max_candy, count)
            else:
                count = 1

    # 열 탐색
    for j in range(n):
        count = 1
        for i in range(1, n):
            if candies[i][j] == candies[i-1][j]:
                count += 1
                max_candy = max(max_candy, count)
            else:
                count = 1

    return max_candy


max_candy = 0
moves = [(1,0), (0,1), (-1,0), (0,-1)]  # 오른쪽, 아래쪽, 왼쪽, 위쪽
for i in range(n):
    for j in range(n):
        for dx, dy in moves:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < n and candies[i][j] != candies[nx][ny]:
                candies[i][j], candies[nx][ny] = candies[nx][ny], candies[i][j]
                # 기존, 바뀐 것 비교
                max_candy = max(max_candy, find_candy_num(candies))
                candies[i][j], candies[nx][ny] = candies[nx][ny], candies[i][j]
print(max_candy)
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
# 치킨 집 m개를 구한다.
# 각각의 치킨집에서 첫번째 집과의 거리가 가장 작은 것을 더함
# 반복
# 모든 치킨 집의 조합을 돌면서
# 한 치킨 집과 home의 차이를 구하고 가장 작은 것들의 합을 구한다.
# 최솟값보다 큰 지 작은지 구하고 크다면 빠르게 종료한다.
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
homes = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            homes.append((i,j))
min_value = float('inf')

for chickens in combinations(chicken,m):
    temp_min_value = 0
    for home in homes:
        queue = deque(chickens)
        distance = float('inf')
        while queue: # 모든 집을 돌면서 최소
            cr, cc = queue.popleft()
            distance = min(distance, abs(cr-home[0])+abs(cc-home[1]))
        temp_min_value += distance
        if temp_min_value >= min_value:
            break
    min_value = min(min_value, temp_min_value)
print(min_value)
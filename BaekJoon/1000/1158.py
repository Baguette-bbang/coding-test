# 백준 1158번 요세푸스 문제 - 실버4
from collections import deque

# 입력
n, k = map(int, input().split())

# 큐 생성
queue = deque()
for i in range(1, n+1):
    queue.append(i)

# pop
cnt = 0
answer = "<"
while queue:
    num = queue.popleft()
    cnt += 1
    if cnt == k:
        cnt = 0
        answer += str(num) + ', '
    else:
        queue.append(num)
print(answer[:-2] + '>')

# 1 2 3 4 5 6 7
# 4 5 6 7 1 2
# 7 1 2 4 5
# 4 5 7 1


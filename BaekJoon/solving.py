# 수빈이는 걷거나 순간이동이 가능하다.
# 걷는다면 1초 후 X-1, X+1로 이동가능하다.
# 순간이동이라면 1초 후 2*X의 위치로 이동한다.
# 결국 brute force문제임
# 너비 우선 탐색으로 풀면 됨.
# 한 스텝마다 세갈래 길이 있음.(뒤로 앞으로 순간이동)
# 종료 조건은 어떻게 되는건가? 도착하거나 도착점에서 2이상 벗어나거나
# 방문하는 시점에 또 방문을 원한다면 그것은 안됨.
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
# N = 5
# K = 17

graph = [[]for _ in range(K+2)]
for i in range(K+2):
    if i == 0:
        graph[i].append(1)
    elif i == K:
        pass
    elif i==K+1:
        graph[i].append(i-1)
    else:
        if i-1 not in graph[i]:
            graph[i].append(i-1)
        if i+1 not in graph[i]:    
            graph[i].append(i+1)
        if i*2 not in graph[i] and i*2 < K+2:
            graph[i].append(i*2)
visit = [False for _ in range(K+2)]

def bfs(graph, start, visit):
  sec = 0
  queue = deque([start])
  visit[start] = True
  # 5와 연결된 4,6,10 저장
  # 4,6,10이 다 빠지면 레벨 추가
  parent = set(graph[start]) 
  while (visit[K]==False) and queue:
    #print(queue)
    n = queue.popleft()
    for i in graph[n]:
      if not visit[i]:
        queue.append(i)
        visit[i]=True
    if not set(queue).intersection(parent):
      parent = set(queue)
      #print("새로운 레벨 :", parent)
      sec += 1
  sec+=1
  print(sec)
bfs(graph, K, visit)
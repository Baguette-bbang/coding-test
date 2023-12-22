from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
e = int(input())
g = [[]for _ in range(n+1)]
for i in range(0,e):
    # 입력받기
    temp1, temp2 = map(int, input().split())
    g[temp1].append(temp2)
    g[temp2].append(temp1)
def dfs(g, s):
    visited = []
    need_visited = deque()
    
    need_visited.append(s)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(g[node])
    return visited

print(len(dfs(g, 1))-1)
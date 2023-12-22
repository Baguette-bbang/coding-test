import sys 
input = sys.stdin.readline

def dfs(g, start, end, path, visited):
    path.append(start)
    visited[start] = True
    
    if start == end:
        return path
    
    for i in g[start]:
        if not visited[i]:
            result_path = dfs(g, i, end, path, visited)
            if result_path:
                return result_path
    #path.pop()
    return None

n = int(input())
start, end = map(int, input().split())
m = int(input())
relationship = [[]for _ in range(n+1)]
for i in range(m):
    temp1, temp2 = map(int, input().split())
    relationship[temp1].append(temp2)
    relationship[temp2].append(temp1)
visited = [False] * (n+1)
path = dfs(relationship, start, end, [], visited)

if path:
    print(len(path) - 1)
else:
    print(-1)

def explore(visited, dungeons, k):
    # 모든 던전을 재귀로 방문
    i = 0 
    max_explored = 0
    for need, use in dungeons:
        if i not in visited and need <=k:
            visited.append(i)
            explored = 1 + explore(visited, dungeons, k-use)
            visited.remove(i)
            max_explored = max(explored, max_explored)
        i+=1
    return max_explored
def solution(k, dungeons):
    return explore([], dungeons, k)
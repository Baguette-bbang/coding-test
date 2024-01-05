import sys
input = sys.stdin.readline
n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

# 한팀만 재귀 돌리고 나머지는 다른 팀에 의해 팀이 결정되는 방식으로 진행
def make_team(ability, n, start, idx, min_diff):
    
    if len(start)*2 == n:
        sa = 0
        la = 0
        link = [i for i in range(n) if i not in start]
        
        for i in start:
            for j in start:
                sa += ability[i][j]
                
        for i in link:
            for j in link:
                la += ability[i][j]

        return min(min_diff, abs(sa-la))

    if idx < n:
        start.append(idx) # 해당 팀원을 넣은 경우
        min_diff = make_team(ability, n, start, idx+1, min_diff)
        start.pop() # 해당 팀원을 넣지 않은 경우
        min_diff = make_team(ability, n, start, idx+1, min_diff)
        
    return min_diff

min_diff = make_team(ability, n, [], 0, float('inf'))
print(min_diff)
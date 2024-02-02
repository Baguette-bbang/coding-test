from collections import deque
def solution(places):
    answer = []
    # 파티션이 사이에 있으면 괜찮다.
    # 응시자는 P, 빈 테이블은 O, 파티션은 X
    # 응시자 상하좌우, 대각선, 위 두 칸, 아래 두 칸, 옆 두 칸, 좌 두 칸 검사
    
    # 유저가 있다면 검사인 것임. 없다면 파티션 여부를 생각하지 않아도 됨.
    # 유저가 있다면?
    # 대각선 아래에 있다면 오른쪽, 아래쪽에 파티션이 있어야함,
    # 대각선 위에 있다면 위쪽, 왼쪽에 파티션이 있어야함,
    
    # 변경 위치 체크 함수 하나
    # P의 위치를 미리 넣어두기
    # 각 강의실 별로 리스트로해서 처리하기
    for room in places:
        graph = []
        for line in room:
            graph.append(list(line))
        
        partition = []
        queue = deque()
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] == 'P':
                    queue.append((i,j))
        
        n = len(graph)
        # 0: 우측, 1:하측
        moves = {0:(0,1),1:(1,0),2:(1,1),3:(2,0),4:(0,2), 5:(1,-1)} # 위에서부터 아래로 순차 탐색이기에 위에는 탐색 안해도됨.
        check_notsafe = False
        while queue: 
            tr, tc = queue.popleft()
            for i in range(len(moves)):
                dr, dc = moves[i]
                nr, nc = tr+dr, tc+dc

                if 0<=nr<n and 0<=nc<n and graph[nr][nc] == 'P':
                    if i == 0 or i == 1:  # 우측 또는 하측이라면 바로 스탑
                        check_notsafe = True
                    elif i==2:
                        # 오른쪽 과 아래쪽이 파티션이 있어야 함
                        if graph[tr+1][tc] != 'X' or graph[tr][tc+1] != 'X':
                            check_notsafe = True
                    elif i==3:
                        # 바로 아래칸에 파티션이 있어야 함
                        if graph[tr+1][tc] != 'X':
                            check_notsafe = True
                    elif i == 4:
                        if graph[tr][tc+1] != 'X':
                            check_notsafe = True
                    else:  # 좌 우측 대각선
                        if graph[tr+1][tc] != 'X' or graph[tr][tc-1] != 'X':    
                            check_notsafe = True

                if check_notsafe:
                    answer.append(0)
                    break  

            if check_notsafe:
                break  
        
        if not check_notsafe: # 정답인 경우                               
            answer.append(1)

    return answer

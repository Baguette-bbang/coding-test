def solution(m, n, board):
    answer = 0
    # 문제 재정의
    # 1. 주변 4칸이 모두 같은 문자인지 확인하기
    # 2. 4칸이 같은 문자인 위치 지우기
    # 3. 지워진 위치 위에 문자가 있다면 내리기  -> 문자열로 형번환 -> replace '0' -> 다시 리스트로
    board = list(map(list, zip(*board[::-1]))) # 행렬 전환
    # 다 왼쪽으로 밀어야함(내리는 행위)
    def check_four():
        moves = [(0,1), (1,0), (1,1)]
        delete_items = []
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                temp_delete = [(i,j)]
                delete_item = board[i][j]
                for di, dj in moves:
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<m and delete_item == board[ni][nj] and board[ni][nj] != '0':
                        temp_delete.append((ni,nj))
                if len(temp_delete) == 4:
                    delete_items += temp_delete
        return delete_items
    
    def make_0(delete_items):
        nonlocal answer
        if len(delete_items) == 0:
            return False
        answer += len(set(delete_items))
        for i,j in list(delete_items):
            board[i][j] = '0'
        return True
    
    def delete_0():
        for idx, line in enumerate(board):
            line = ''.join(line).replace('0', '')
            line += (m - len(line)) * '0'
            board[idx] = list(line)
            
    while True:
        delete_items = check_four()
        if not make_0(delete_items):
            break
        delete_0()
        
    return answer
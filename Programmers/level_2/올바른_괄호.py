from collections import deque
def solution(s):
    answer = False
    # 스택에 (가 들어오면 )가 해당 개수만큼 출현해야한다.
    # )가 출현 시 현재 스택의 개수를 구하고 해당 개수만큼 출현하는지 확인한다.
    stack = deque(s)
    cnt = 0
    
    while stack:
        gual = stack.popleft()
        if gual == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return answer
        
    if cnt != 0:
        return answer
    return True
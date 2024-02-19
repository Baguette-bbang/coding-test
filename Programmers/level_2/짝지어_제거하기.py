from collections import deque
def solution(s):
    queue = deque()
    
    for c in s:
        
        if queue and queue[-1] == c:
            queue.pop()
        else:
            queue.append(c)
            
    if queue:
        return 0
    else:
        return 1
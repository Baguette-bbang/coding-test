from collections import deque
from math import ceil
def solution(progresses, speeds):
    # 40분 시작 53분 끝 (소요시간 13분)
    answer = []
    tasks = deque()
    n = len(progresses)
    for i in range(n):
        tasks.append(ceil((100-progresses[i])/speeds[i]))
    
    answer.append(1)
    last = tasks.popleft()
    while tasks:
        temp = tasks.popleft()
        if last >= temp:
            answer[-1] += 1
        else:
            last = temp
            answer.append(1)
            
    return answer
from collections import deque
def solution(s):
    # 문자인가?
    answer = ''
    queue = deque(list(s))
    temp = ''
    while queue:
        c = queue.popleft()
        if c != ' ':
            temp += c
        else:
            if len(temp) > 0:
                answer+=temp[0].upper() + temp[1:].lower()
            temp = ''
            answer += c
    if len(temp) > 0:
        answer+=temp[0].upper() + temp[1:].lower()
    return answer
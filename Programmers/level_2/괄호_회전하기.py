from collections import deque
def solution(s):
    answer = 0
    # 안의 괄호가 잘못되면 밖의 괄호도 잘못된 괄호이다.
    open = ['[', '{', '(']
    def check_bracket(s):
        queue = deque()
        for i in range(len(s)):
            if s[i] in open:
                queue.append(s[i])
            else:
                if not queue:
                    return False
                if s[i] == ']':
                    close = queue.pop()
                    if close != '[':
                        return False
                elif s[i] == '}':
                    close = queue.pop()
                    if close != '{' :
                        return False 
                elif s[i] == ')':
                    close = queue.pop()
                    if close != '(':
                        return False 
        if queue: # 짝이 맞지 않는 경우
            return False
        return True
    
    for i in range(len(s)):
        if check_bracket(s):
            answer += 1
        s = s[1:] + s[0]
    return answer
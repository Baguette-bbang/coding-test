import sys
input = sys.stdin.readline

def format_exp(exp):
    formatted_exp = ''
    in_number = False  
    for char in exp:
        if char.isdigit():
            if in_number:  # 연속된 숫자의 경우
                formatted_exp += ' ' + char

            else:  # 새 숫자의 시작인 경우
                formatted_exp += char
                in_number = True
        else:
            formatted_exp += char
            in_number = False  
    return formatted_exp

def dfs(v, exp):
    visited[v] = True
    # 1~N까지의 숫자에 대해 부호를 한번씩 돌면서
    for s in sign:
        new_exp = exp + s + str(lst[v])
        if v == N-1: # 만약 N값(마지막값)에 도달한다면
            if cal(new_exp) == 0: # 마지막값까지 연산했을때 0이라
                expressions.append(format_exp(new_exp)) # 수식 출력
        elif not visited[v+1] : # 아직 마지막값에 도달하지 않았다면 다음 수식을 계속 구한다
            dfs(v+1, new_exp)
    visited[v] = False

def cal(exp):
    total = 0
    num=''
    op= 1
    for char in exp:
        if char.isdigit():
            num += char
        else:
            total += op * int(num) if num else 0
            num = ''
            op = 1 if char == '+' else -1
    total += op * int(num) if num else 0  # 마지막 숫자를 추가
    return total
test = int(input())
expressions = []
fianal_expressions = []

for _ in range(test):
    N = int(input())
    lst = [i for i in range(1, N+1)]
    sign = ["+", "-", ""]
    visited = [False for _ in range(0, N)]
    dfs(1,str(lst[0]))
    expressions.sort()  
    for exp in expressions:
        fianal_expressions.append(exp)
    expressions.clear()
    fianal_expressions.append(" ")

for answer in fianal_expressions:
    print(answer)

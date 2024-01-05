from copy import deepcopy

def cal(a, op, b):
    if op == '-':
        return a - b
    elif op == '+':
        return a + b
    elif op == '*':
        return a * b

def solution(expression):
    answer = 0
    operators = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '+', '-'], ['*', '-', '+']]
    
    # 문자열을 숫자와 연산자로 분리작업을 먼저 해야함
    # 그리고 저장된 순서에 맞게 계산을 진행하면서 최대절대값을 찾으면 됨
    expression_list = []
    number = ''
    for char in expression: # 연산자와 숫자를 구분
        # 연산자가 나올때까지 number에 + 시키고 한번에 할당
        if char.isdigit(): 
            number += char
        else:
            expression_list.append(int(number)) # 정수
            expression_list.append(char) # operator
            number = ''
    expression_list.append(int(number)) # 마지막은 숫자이기에 
    # print(expression_list)
    max_num = 0
    for operator in operators: # 연산자 우선순위에 따른 리스트
        temp_expression = deepcopy(expression_list)
        for op in operator: # 각 우선순위에 해당하는 연산자를 먼저 작업
            i = 0 # 앞에서부터 반복
            while i < len(temp_expression):
                # print(temp_expression,i)
                if temp_expression[i] == op: # 먼저 계산하고싶은 연산자라면
                    result = cal(temp_expression[i-1], temp_expression[i], temp_expression[i+1])
                    temp_expression[i-1:i+2] = [result]  # 계산된 결과로 리스트값을 치환
                    i -= 1 
                else:
                    i += 1
        max_num = max(max_num, abs(temp_expression[0]))

    return max_num
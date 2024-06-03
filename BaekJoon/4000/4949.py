# 4949번 실버4 균형잡힌 세상 스택 문제
# 4종류의 괄호가 등장한다. 
# 닫히는 괄호가 등장했다면 같은 종류의 열리는 괄호가 있는지 확인
# 없다면 실패
# 괄호가 남았다면 실패
while (1):
    sentence = input()
    if sentence == '.':
        break
    stack = []
    flag = True
    for c in sentence:
        if c == '[' or c == '(':
            stack.append(c)
        elif c == ']' or c == ')':
            if not stack :
                print('no')
                flag = False
                break
            elif c == ']' and stack.pop() == '[':
                continue
            elif c == ')' and stack.pop() == '(':
                continue
            else:
                print('no')
                flag = False
                break
    if stack and flag:
        print('no')
    elif flag :
        print('yes')
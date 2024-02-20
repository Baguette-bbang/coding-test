from collections import deque
def solution(numbers):
    stack = deque()
    n = len(numbers)
    answer = [-1] * n
    # 로직
    # 스택의 마지막 요소와 현재 요소와 같다면 pop하고 해당 위치에 numbers[i]를 넣기
    for i in range(n):
        num = numbers[i]
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            answer[idx] = num
        stack.append(i)
    print(stack)
    return answer
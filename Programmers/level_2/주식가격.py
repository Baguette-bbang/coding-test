from collections import deque
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = deque([0]) # 초기화
    # 로직
    # 인덱스를 스택에다가 담는다.
    # 스택의 마지막 요소가 
    # 시간은 0초부터 n초까지로 구성 하나 요소를 추가할때마다 스택의 제일 마지막 요소와 비교 
    # 스택의 요소가 더 크다면 스택을 pop 하고 앤서의 해당 위치에 시간을 적는다.
    for i in range(1,n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = n-1 - idx
    return answer

# 백준 10828 실버4 스택 문제
# 시작 17시 12분
# 종료 17시 23분
from collections import deque
import sys
input = sys.stdin.readline
stack = deque()
for _ in range(int(input())):
    order = input().split()
    if order[0] == 'push' :
        stack.append(int(order[1]))
    elif order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
from math import ceil
def solution(n,a,b):
    answer = 0
    while True:
        if abs(a-b) == 0:
            return answer
        else:
            answer += 1
            a, b = ceil(a/2), ceil(b/2)
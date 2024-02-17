def solution(n):
    answer = n
    n1_1 = format(n, 'b').count('1')
    print(n1_1)
    while True:
        answer += 1
        n2_1 = format(answer, 'b').count('1')
        if n1_1 == n2_1:
            return answer
    
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    i = m-1
    while i < len(score):
        answer += score[i] * m
        i += m
    return answer
def solution(k, score):
    answer = []
    new_score = []
    for i in score:
        new_score.append(i)
        new_score.sort(reverse = True)
        if len(new_score) > k:
            new_score.pop()
        answer.append(new_score[-1])
    return answer
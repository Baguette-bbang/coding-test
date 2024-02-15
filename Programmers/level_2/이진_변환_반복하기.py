def solution(s):
    answer = []
    while len(s) > 1:
        length1 = len(s)
        # print(s)
        s = s.replace("0",'')
        length2 = len(s)
        answer.append(length1 - length2)
        s = format(length2, 'b')
    return [len(answer), sum(answer)]
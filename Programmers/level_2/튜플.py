def solution(s):
    answer, new_tuples = [], []
    tuples = s.lstrip('{').rstrip('}').split("},{")
    
    for s in tuples:
        s = list(map(int, s.replace("{",'').replace("}",'').split(',')))
        new_tuples.append(s)
    new_tuples.sort(key = len)
    
    for s in new_tuples:
        for c in s:
            if c not in answer:
                answer.append(c)
                
    return answer
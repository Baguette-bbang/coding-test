def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    n = len(answers)
    
    c1, c2 ,c3 = 0,0,0
    for i in range(n):
        i1 = i%len(s1)
        i2 = i%len(s2)
        i3 = i%len(s3)
        if s1[i1] == answers[i]:
            c1+=1
        if s2[i2] == answers[i]:
            c2+=1
        if s3[i3] == answers[i]:
            c3+=1
            
    result = [c1,c2,c3]
    result.sort()
 
    if result[-1] == c1:
        answer.append(1)
    if result[-1] == c2:
        answer.append(2)
    if result[-1] == c3:
        answer.append(3)
        
    return answer
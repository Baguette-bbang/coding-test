def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
  
    for los in range(1,n+1):
        if los in reserve and los in lost:
            reserve.remove(los)
            lost.remove(los)
    
    for los in range(1, n+1):
        if los in lost:
            if los-1 in reserve:
                answer += 1
                reserve.remove(los-1)
            elif los+1 in reserve:
                answer += 1
                reserve.remove(los+1)
    
    return n - len(lost) + answer 
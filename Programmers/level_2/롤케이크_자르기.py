from collections import Counter
def solution(topping):
    answer = 0
    # 43분 시작 -> 11분 종료 (28분 소요)
    # 투포인터 사용
    topping_count = Counter(topping)
    left = set()
    right = len(topping_count)
    
    for i in range(len(topping)): # 종료조건 1
        # set은 in 연산이 빠름 계속 추가하는 것보다는 나음
        if topping_count[topping[i]] >= 1 and topping[i] not in left:
            left.add(topping[i])
            
        topping_count[topping[i]] -= 1
        
        if topping_count[topping[i]] == 0:
            right -= 1
            
        if len(left) == right:
            answer += 1
            
        elif len(left) > right: # 종료조건 2
            break
        
    return answer
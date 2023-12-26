def solution(numbers, target):
    answer = 0
    
    #초기값 설정
    cal_list = []
    cal_list.append(numbers[0])
    cal_list.append(-numbers[0])
    
    # 모든 경우의 수 탐색
    for i in range(1,len(numbers)): 
        temp = []
        for num in cal_list: 
            temp.append(num+numbers[i])
            temp.append(num-numbers[i])
        cal_list = temp
    
    # 모든 계산된 값들 중 target과 일치하는 값의 개수를 return
    answer = cal_list.count(target)
    return answer
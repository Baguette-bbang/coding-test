# 풀이1
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
#########################################################
# 풀이2
def DFS(numbers, target, idx, num, length):
    global answer
    if idx == length:
        if num == target:
            answer += 1
        return
    
    DFS(numbers, target, idx+1, num+numbers[idx], length)
    DFS(numbers, target, idx+1, num-numbers[idx], length)
    return 
def solution(numbers, target):
    global answer
    answer = 0
    length = len(numbers)
    DFS(numbers, target, 0, 0, length)
    return answer
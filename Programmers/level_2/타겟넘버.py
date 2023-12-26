def solution(numbers, target):
    answer = 0
    # 각 number마다 부호를 추가해서 2차원 행렬로 만듦.
    graph = [[] for _ in range(len(numbers))]
    for i in range(len(numbers)):
        graph[i].append(numbers[i])
        graph[i].append(numbers[i]*-1)
    
    # 계산된 값을 저장하기 위한 리스트 초기화
    queue = []
    queue.append(graph[0][0])
    queue.append(graph[0][1])
    
    # 모든 경우의 수 탐색
    for i in range(1,len(numbers)): 
        temp = []
        for num in queue: 
            for z in range(2):
                temp.append(num+graph[i][z])
        queue= temp
    
    # 모든 계산된 값들 중 target과 일치하는 값의 개수를 return
    for i in queue:
        if i == target:
            answer +=1
    return answer
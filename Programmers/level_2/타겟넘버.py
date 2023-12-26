def solution(numbers, target):
    answer = 0
    graph = [[] for _ in range(len(numbers))]
    for i in range(len(numbers)):
        graph[i].append(numbers[i])
        graph[i].append(numbers[i]*-1)
    queue = []
    queue.append([graph[0][0], graph[0][1]])
    for i in range(1,len(numbers)): 
        number = queue.pop(0)
        temp = []
        for num in number: 
            for z in range(2):
                temp.append(num+graph[i][z])
        queue.append(temp)
    
    for i in queue[0]:
        if i == target:
            answer +=1
    return answer
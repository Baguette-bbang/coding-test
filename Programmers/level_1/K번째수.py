def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]
        k = commands[i][2]
        answer.append(sorted(array[start:end])[k-1])
    return answer
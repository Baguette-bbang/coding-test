def solution(rows, columns, queries):
    answer = []
    graph = []
    num = 1
    for i in range(rows):
        graph.append([j for j in range(num, num+columns)])
        num = graph[i][-1] + 1
    
    def rotation(query):
        start_r = query[0] - 1
        start_c = query[1] - 1
        end_r = query[2] - 1 
        end_c = query[3] - 1

        # 임시 변수에 첫 번째 요소 저장
        temp = graph[start_r][start_c]
        min_value = temp

        # 상으로 이동
        for i in range(start_r, end_r):
            # 왼쪽 열
            graph[i][start_c] = graph[i+1][start_c]
            min_value = min(min_value, graph[i][start_c])

        # 좌로 이동 
        for i in range(start_c, end_c):
            # 아래쪽 행
            graph[end_r][i] = graph[end_r][i+1]
            min_value = min(min_value, graph[end_r][i])

        # 하로 이동
        for i in range(end_r, start_r, -1):
            # 오른쪽 열
            graph[i][end_c] = graph[i-1][end_c]
            min_value = min(min_value, graph[i][end_c])

        # 우로 이동
        for i in range(end_c, start_c, -1):
            # 위쪽 행
            graph[start_r][i] = graph[start_r][i-1]
            min_value = min(min_value, graph[start_r][i])

        graph[start_r][start_c+1] = temp
        return min_value

    for query in queries:
        answer.append(rotation(query))
    # for g in graph:
    #     print(g)
    return answer
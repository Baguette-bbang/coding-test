def solution(n, costs):
    # 1. 인접 노드 생성
    # 2. 최소 비용 트리 생성
    graph = [[float('inf')] * n for _ in range(n)]
    for i in range(len(costs)):
        graph[costs[i][0]][costs[i][1]] = costs[i][2]
        graph[costs[i][1]][costs[i][0]] = costs[i][2]
    
    MST = set([costs[0][0]])
    answer = 0
    
    while len(MST) < n:
        min_cost = float('inf')
        min_node = None
        
        for node1 in MST:
            for node2 in range(n):
                if node2 not in MST and graph[node1][node2] < min_cost:
                    min_node = node2
                    min_cost = graph[node1][node2]
                    
        answer += min_cost
        MST.add(min_node)
    
    return answer
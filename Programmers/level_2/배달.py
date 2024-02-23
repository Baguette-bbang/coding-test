from heapq import heappop, heappush
def solution(N, road, K):
    answer = 0
    # 가중치가 있는 그래프
    # 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달하려고 함
    # 다익스트라로 1번 정점에서 각 정점까지의 최소비용 거리 업데이트해야함
    graph = [[] for _ in range(N+1)]
    for node1, node2, cost in road:
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))
    
    routes = [float('inf')] * (N+1)
    routes[1] = 0
    queue = []
    heappush(queue, (1,0)) # 정점 거리
    
    while queue:
        cur_node, cur_cost = heappop(queue)
        if routes[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cost + cur_cost
            if new_cost < routes[node]:
                routes[node] = new_cost
                heappush(queue, (node, new_cost))
                
    for route in routes[1:]:
        if route <= K:
            answer += 1
            
    return answer
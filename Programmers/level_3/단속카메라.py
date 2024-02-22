def solution(routes):
    answer = 1
    # 단속용 카메라를 한 번은 만나도록 카메라를 설치
    # 겹치는 지점을 만들어야함.
    # 겹치는 구간이라는 의미는?
    # 현재 이동경로의 진출시점이 다음 이동경로의 진입시점보다 크거나 같아야함.
    routes = sorted(routes, key = lambda x : x[1])
    loc = routes[0][1]
    for i in range(1, len(routes)):
        if loc < routes[i][0]: # 겹치지 않는다면 
            answer += 1
            loc = routes[i][1]            
    return answer
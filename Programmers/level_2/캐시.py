from collections import defaultdict
def solution(cacheSize, cities):
    answer = 0
    # 딕셔너리에 넣고 방문하면서 넣고 정렬하고 기존것을 0으로 만들고
    new_cities = []
    for i in range(len(cities)): # 대소문자 구분 없이 처리
        new_cities.append(cities[i].lower())
    cities_dict = defaultdict(int)
    
    if cacheSize == 0: # 예외 처리
        return len(cities) * 5
    
    for i in range(len(new_cities)):
        cache = sorted(cities_dict.items(), key = lambda x : x[1])
        if cities_dict[new_cities[i]] == 0: # 비어 있다면
            answer += 4
            if len(cache) == cacheSize: # 추가하려는데 꽉 차있다면
                del cities_dict[cache[0][0]]
        cities_dict[new_cities[i]] = i+1
        answer += 1

    return answer
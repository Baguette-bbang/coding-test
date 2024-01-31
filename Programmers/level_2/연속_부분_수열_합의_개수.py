def solution(elements):
    answer = 0
    # 부분 수열이라는 것은 
    # 길이가 1인 것부터 길이가 5인 것까지 조합을 구하면 되는거 아닌가? 실패.ㅠ(시간초과)
    # 연속되어야 하는구나..
    # 값이 포함되었던 것에서 또 포함하면 안됨. 조합의 수를 구하는 문제가 아님. 즉, dp로 푸는게 아님.
    # 하나를 선택하고 n개를 선택하는 문제 하지만 중복이 되어선 안됨.
    # set자료형 쓰기.
    # 순차적으로 돌면서 하나를 선택. 그 다음 n개까지 하나씩 더함.
    # 어차피 선택할 수 있는 것은 최대 n개임 
    # 배열 슬라이싱은 나머지 형태로 구현하기.
    
    sum_subset = set()
    n = len(elements)
    for i in range(n):
        # 요소를 하나 선택하고 다음번 n개를 순차적으로 선택 sum 하면서
        sum_num = 0
        for j in range(i,i+n):
            sum_num += elements[j%n]
            sum_subset.add(sum_num)
    return len(sum_subset)
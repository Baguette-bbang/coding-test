# 최대 2명 제한.
# 무게 제한이 넘으면 같이 탈 수 없음
# 구명보트를 최대한 적게 사용해서 모든 사람을 구출
def solution(people, limit):
    answer = 0
    left = 0 
    right = len(people)-1
    people.sort()
    # 혼자서 타야하는 경우(무게가 딱 맞는 사람인 경우)
    for i in range(len(people)-1, 0,-1):
        if people[i] == limit:
            right -= 1
            answer+=1
        else :
            break
            
    while(right > left):
        # print("right:", people[right])
        # print("left:",people[left])
        # print("answer:", answer)
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
        else :
            right -= 1
            answer += 1
    
    if left == right:
        answer += 1
    return answer

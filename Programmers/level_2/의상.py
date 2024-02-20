from collections import defaultdict
def solution(clothes):
    answer = 1
    # 옷의 종류
    # 각 자리에는 입을 수도 있고 안입을 수도 있다.
    # 안입는 경우 + 해당 옷의 종류
    clothes_dict = defaultdict(int)
    for cloth in clothes:
        clothes_dict[cloth[1]] += 1
    for n in clothes_dict.values():
        answer *= (n+1)
    return answer-1
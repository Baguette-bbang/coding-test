from collections import defaultdict
def solution(friends, gifts):
    # 주고 받은 선물 기록 및 선물 지수 계산
    gifts_records = defaultdict(lambda: defaultdict(int))
    gift_indices = defaultdict(int)

    for gift in gifts:
        give, get = gift.split()
        gifts_records[give][get] += 1
        gift_indices[give] += 1
        gift_indices[get] -= 1

    # 다음 달 선물 예측
    next_month = defaultdict(int)
    for i, friend1 in enumerate(friends):
        for friend2 in friends[i+1:]:
            gifts_diff = gifts_records[friend1][friend2] - gifts_records[friend2][friend1]
            indices_diff = gift_indices[friend1] - gift_indices[friend2]

            if gifts_diff > 0 or (gifts_diff == 0 and indices_diff > 0):
                next_month[friend1] += 1
            elif gifts_diff < 0 or (gifts_diff == 0 and indices_diff < 0):
                next_month[friend2] += 1

    # 결과 계산
    return max(next_month.values(), default=0)
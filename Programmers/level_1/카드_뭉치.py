def solution(cards1, cards2, goal):
    answer = ''
    # 각 카드뭉치의 현재 인덱스를 저장한다.
    # 순차적으로 돌아가며 현재 내가 쓸 수 있는 카드인지 확인한다
    cards1_idx, cards2_idx = 0, 0
    
    for word in goal:
        if cards1_idx < len(cards1) and cards1[cards1_idx] == word:
            cards1_idx += 1
        elif cards2_idx < len(cards2) and cards2[cards2_idx] == word:
            cards2_idx += 1
        else:
            return "No"
    return "Yes"
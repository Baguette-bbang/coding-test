from itertools import permutations,permutations_with_replacement, product
def solution(users, emoticons):
    answer = []
    # 서비스 가입자, 판매액 최대화
    
    # 일정 비율 이상 할인하는 이모티콘을 모두 구매(할인율은 10%, 20%, 30%, 40% 중 하나)
    
    # 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 
    # 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입
    # 가격은 100의 배수
    
    # 1. 할인율 하나 선택 후 이모티콘 가격 설정 딕셔너리 화
    # 2. 딕셔너리 하나 추출
    # 3. 유저 전체 탐색
        # 1. 유저가 구매하는 이모티콘 비용의 합
        # 2. 유저가 구매한 이모티콘 비용의 합이 설정비용보다 적은가?
            # 1. 맞다면 이모티콘 총 구매 비용에 +
            # 2. 아니라면 이모티콘 플러스 서비스 가입자에 +
    discounts = [10, 20, 30, 40]
    discount_dict = {}
    for discount in discounts:
        temp = []
        for emoticon in emoticons:
            temp.append(emoticon // 100  * (100-discount))
        discount_dict[discount] = temp

    # 이모티콘마다 10~40퍼센트 할인을 해야함.

    sale = [] # 플러스 가입자, 매출액 저장
    for discounts in list(product(discounts, repeat=len(emoticons))):
        # 할인율에 해당하는 이모티콘 값을 가져오기
        # discounts에는 이모티콘 당 할인율이 적혀 잇음
        new_emoticons = []
        for i in range(len(emoticons)):
            new_emoticons.append((discounts[i], discount_dict[discounts[i]][i]))
        # 할인율당 이모티콘의 가격으로 저장
        gudok = 0 # 구독자 수
        total_purchase = 0 # 특정 할인율로 구매하는 모든 유저들의 이모티콘 금액
        for j in range(len(users)):
            purchase = 0 # 유저 한명이 구매하는 이모티콘의 금액
            for k in range(len(new_emoticons)):
                if users[j][0] <= new_emoticons[k][0]: # 특정 할인율 이상이라면 구매
                    purchase += new_emoticons[k][1]                         
            if purchase >= users[j][1]:
                gudok += 1
            else:
                total_purchase += purchase
        sale.append((gudok, total_purchase))
    sale.sort()
    print(len(sale))
    answer = [sale[-1][0],sale[-1][1]]
    return answer

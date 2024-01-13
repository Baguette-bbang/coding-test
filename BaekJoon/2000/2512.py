# 입력
n = int(input()) # 예산을 할당받고자 하는 사람의 수
request_budgets = list(map(int, input().split())) # 예산 요청액들
limit_budget = int(input()) # 총 가용 예산

start = 1 # 시작 예산(최소값 1)
end = max(request_budgets) 
max_budget = 0
while start<=end: # 종료조건 
    base_budget = (start+end) // 2 
    use_budget = 0
    for budget in request_budgets:
        if budget <= base_budget: # 사용하려는 예산이 기준 예산 이하라면
            use_budget += budget # 사용하려는 예산만큼 더해도 됨.
        else: # 예산이 기준예산보다 위라면 기준예산밖에 못 쓴다.
            use_budget += base_budget
    # 또는 예산이 너무 많아서 기준 예산을 쓸데없이 크게 잡은 경우
    if use_budget > limit_budget: # 사용 예산이 리미트 예산 초과라면
        end = base_budget - 1 # 사용할 예산 범위를 줄여야함.
    else: # 사용 예산이 리미트 예산 이하라면
        max_budget = base_budget # 사용한 예산은 무조건 리미트 예산 이하여야하기에 여기서 max값 업데이트
        start = base_budget + 1 # 사용할 예산 범위를 늘려야함.
print(max_budget)

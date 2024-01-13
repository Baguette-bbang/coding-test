def solution(n, k, enemy):
    answer = 0
    start = 1
    end = len(enemy) # 진행 가능한 최대한의 라운드
    # 먼저 무적권을 다 활용해서 라운드를 끝낼 수 있다면 그렇게 끝낸다. 
    # 사실 없어도 되긴하다.
    if len(enemy) <= k: 
        answer = len(enemy)
    else: 
        while start <= end: # 종료조건 설정
            round = (start+end) // 2 # 진행 가능한 round 설정
            # 역정렬을 하여 앞에서부터 k개의 무적권을 사용
            round_list = sorted(enemy[:round], reverse=True)
            
            if round > k: # 무적권을 다 사용해도 라운드가 남았다면
                round_list = round_list[k:] 
            else:
                round_list = []
                
            # k번부터 끝까지 라운드를 진행    
            remaining = n
            for round_enemy in round_list: # 무적권을 사용하고 남은 적들을 무찌름
                remaining -= round_enemy

            if remaining >= 0: # 아직 충분히 무찌를 수 있다면
                start = round+1
                answer = round
            else: # 적이 너무 많아서 무찌르지 못한다면
                end = round-1
    return answer
# --------------------------------------------------------------------------------
import heapq

def solution(n, k, enemy):
    # 최대 힙 생성
    # 파이썬에서는 최소힙만 지원하기에 -를 취해서 힙에 넣어줘야한다.
    max_heap = [-e for e in enemy]
    heapq.heapify(max_heap)

    rounds = 0
    while max_heap: # 힙이 비어있지 않은 동안 라운드를 진행한다.
        # 무적권 사용
        if k > 0: # 각 라운드에서 무적권 k가 남아있다면, 힙에서 가장 강한 적(최대 값)을 제거
            heapq.heappop(max_heap)
            k -= 1
        else:
            # 남은 적은 병사를 가용해 싸움
            n += heapq.heappop(max_heap)  # 최대 힙이므로, 값을 더할 때 부호를 바꿈
            if n < 0:
                break  # 병사가 부족할때까지 반복한다. 

        rounds += 1

    return rounds

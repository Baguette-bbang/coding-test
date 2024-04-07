from heapq import heappush, heappop, heapify
def solution(book_time):
    answer = 0
    # 최소한의 객실만을 사용하여 예약 손님들을 받으려고 한다.
    # 손님이 객실을 이용 후 객실을 10분 청소해야함.
    # 1. 종료시간에 10분 더하기
    # 2. 시작 시간으로 정렬하기
    # 3. 종료시간이 가장 빠른 것으로 heapsort
    # 4. 새로운 대실 시작시간이 가장 종료시간이 빠른 것보다 작다면 answer += 1 대신 길이로서 수행함.

    # 1. 종료 시간 + 10분 하기
    new_book_time = []
    for start, end in book_time:
        start = int(start.replace(":",""))
        end = int(end.replace(":","")) + 10
        if end%1000%100 >= 60:
            end = end - 60 + 100
        new_book_time.append([start, end])
        
    # 2. 시작 시간으로 정렬하기
    new_book_time.sort(key=lambda x : x[0])
    
    # 3. 종료 시간이 가장 빠른 것으로 heapsort하기
    heap = []
    # 전의 종료시간이 현재의 시작시간보다 작거나 같으면 빼고 다시 넣지 않아도 된다.
    for start, end in new_book_time:
        if heap:
            prev = heappop(heap)
            if prev > start:
                heappush(heap, prev)
        heappush(heap, end)
    
    return len(heap)
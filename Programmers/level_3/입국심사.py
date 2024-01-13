def solution(n, times):
    answer = 0
    # waiting_time = []
    # for i in range(1,n+1):
    #     for time in times:
    #         waiting_time.append(time*i)
    # waiting_time.sort()
    # 모든 가능한 수, 즉, times의 마지막 값에 n만큼 기다린 시간
    end = max(times)*n
    start = 1
    min_n = 0
    while start <= end:
        mid = (start+end)//2
        # 7이나 10으로 나누어 떨어지는가?
        # 나누어 떨어지는 수 중 값을 좁히거나 늘리기 위해서는 어떤 조건이 필요?
        # 4+2 = 6
        num = sum(mid//time for time in times)
        if num >= n: 
            # 줄어야 함.
            end = mid - 1
            min_n = mid
        else:
            start = mid + 1
    return min_n
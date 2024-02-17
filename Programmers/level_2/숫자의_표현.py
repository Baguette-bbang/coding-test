def solution(n):
    answer = 1
    for i in range(1, n):
        temp_n = i
        for j in range(i+1, n-i+1):
            temp_n+=j
            if temp_n == n:
                answer += 1
                break
            if temp_n > n:
                break
    return answer
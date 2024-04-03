def solution(storey):
    answer = 0
    # 형변환하고 뒤에서부터 탐색
    # 5보다 작다면 빼고 5보다 크다면 더한다 5라면 그 앞의수를 보고 결정한다.
    while storey:
        last_num = storey%10
        if last_num == 5 and storey//10%10 >= 5 or last_num > 5 :
            storey += 10 - last_num
            answer += 10 - last_num
        else:
            answer += last_num
        storey //= 10
        
    return answer
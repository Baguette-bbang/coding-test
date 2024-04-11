def solution(data, col, row_begin, row_end):
    answer = 0
    # 1. 정렬 
    data.sort(key = lambda x : (x[col-1], -x[0]))

    # 2. mod 수행하기
    mod_arr = []
    for i in range(row_begin-1, row_end):
        mod = 0
        for j in data[i]:
            mod += j%(i+1)
        mod_arr.append(mod)    
    
    # 3. XOR 연산 (둘 중 하나만 1이 아니여야 함)
    for i in mod_arr:
        answer ^= i
    return answer
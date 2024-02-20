def solution(n, t, m, p):
    answer = ''
    # 시작:정각, 종료:29
    n_jinsu = '0'
    bigger_10 = {}
    for i in range(16):
        bigger_10[i+10] = chr(65+i)

    for i in range(1,t*m):
        if len(n_jinsu) >= t*m:
            break
        temp = ''
        while i:
            mod = i % n
            i //= n
            if mod < 10:
                temp += str(mod)
            else:
                temp += bigger_10[mod]
        n_jinsu += temp[::-1]

    p -= 1
    for i in range(t):
        answer += n_jinsu[p+m*i]
    return answer
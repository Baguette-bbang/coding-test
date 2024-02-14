def solution(today, terms, privacies):
    # 유효기간 전까지만 보관 가능하다.
    # 먼저 privacies를 스플릿하고 인트로 바꾼다.
    # terms를 딕셔너리로 바꾼다.
    # 각 privacies 마다의 계약 만료 일자를 구한다.
    answer = []
    term_dict = {}
    for term in terms:
        a,b = term.split()
        term_dict[a] = int(b)    
    # 오늘 날짜 스플릿
    ty, tm, td = map(int, today.split('.'))

    for idx, privacy in enumerate(privacies):
        py, pm, pd = map(int, privacy.replace('.', ' ').split()[:-1])
        pt = privacy[-1]
        # 유효기간 계산
        pm += term_dict[pt]
        py += (pm - 1) // 12 
        pm = (pm - 1) % 12 + 1
        
        # 유효기간의 마지막 날짜 계산
        pd -= 1
        if pd == 0:
            pm -= 1
            if pm == 0:
                py -= 1
                pm = 12
            pd = 28 

        # 만료 햇는가???
        if (py, pm, pd) < (ty, tm, td):
            answer.append(idx + 1)

    return answer

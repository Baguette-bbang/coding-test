# "#" 처리를 하는 것이 이 문제의 관건이다.
def solution(m, musicinfos):
    answer = "(None)"
    max_length = 0
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        
        # 1. 시간 차 구하기
        start = list(map(int, musicinfo[0].split(':')))
        end = list(map(int, musicinfo[1].split(':')))
        start = start[0] * 60 + start[1]
        end = end[0] * 60 + end[1]
        time_diff = end - start
        
        # 2. 악보 재정립하기 ("#" 처리하기)
        score = []
        for i in range(len(musicinfo[3])):
            if musicinfo[3][i] == "#":
                score[-1] += "#"
            else:
                score.append(musicinfo[3][i])
        
        m_score = []
        for i in range(len(m)):
            if m[i] == "#":
                m_score[-1] += "#"
            else:
                m_score.append(m[i])

        # 3. 악보 늘리기
        if len(score) >= time_diff:
            score = score[:time_diff]
        else:
            score = (score * time_diff)[:time_diff]
        
        # 4. 일치 여부 확인하기
        if ', '.join(m_score)+',' in ', '.join(score)+',' and max_length < time_diff:
            max_length = time_diff
            answer = musicinfo[2]
        
    return answer
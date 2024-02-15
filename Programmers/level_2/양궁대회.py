def solution(n, info):
    archery_target = [0] * 11
    answer = [-1]
    max_diff = 0

    def recursion(left_arrow, cur_location, archery_target):
        nonlocal max_diff, answer
        # 종료조건
        # 화살을 다 썼거나, 과녁의 끝에 도달했거나
        if left_arrow==0 or cur_location==10:
            archery_target[-1] = left_arrow
            # 점수차이 계산
            apeach = 0
            ryan = 0 
            for i in range(11):
                if info[i] == 0 and archery_target[i] == 0:
                    continue
                if info[i] >= archery_target[i]:
                    apeach += 10-i
                else:
                    ryan += 10-i
            if ryan > apeach:
                diff = ryan - apeach
                if diff > max_diff:
                    max_diff = diff
                    answer = [archery_target.copy()]
                elif diff == max_diff:
                    answer.append(archery_target.copy())
            return
        else:
            # 현재 위치의 과녁을 방문하지 않는 경우
            recursion(left_arrow, cur_location+1, archery_target)
            # 현재 위치의 과녁을 방문하는 경우
            if left_arrow > info[cur_location]:
                temp_archery_target = archery_target.copy()
                left_arrow -= (info[cur_location]+1)
                temp_archery_target[cur_location] = info[cur_location]+1
                recursion(left_arrow, cur_location+1, temp_archery_target)
                
    recursion(n, 0, archery_target)
    new_answer = []
    if max_diff>0:
        for i in answer:
            new_answer.append(i[::-1])
        new_answer.sort()
        return new_answer[-1][::-1]
    else:
        return [-1]

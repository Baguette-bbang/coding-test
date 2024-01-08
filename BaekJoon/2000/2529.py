def make_inequality_signs_num(n, current, visited, inequality_signs, max_num, min_num):
    # 비교 후 조건에 맞고 가장 작거나 크다면 기존 값을 업데이트 
    # 종료조건은 현재 길이가 n-1이 된다면 종료
    # n의 역할 : 길이
    # idx의 역할 : 방문할 숫자
    # current의 역할 : 현재 부등호에 맞게 만들어진 문자열
    # visited의 역할 : 방문한 숫자
    # inequality_signs : 방문해야할 부등호 리스트
    length = len(current)
    if length == n: # 
        num = int(current)
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return max_num, min_num
    for i in range(10):
        if i not in visited : # 0~9사이이고 중복되지 않는 숫자라면
            # 조건 체크 부등호 안에 들어와야 함.
            visited.append(i)
            if length > 0:
                if inequality_signs[length-1] == '<' and int(current[-1]) < i:
                    max_num, min_num = make_inequality_signs_num(n, current+str(i), visited, inequality_signs, max_num, min_num)

                elif inequality_signs[length-1] == '>' and int(current[-1]) > i: # '>' 인 경우
                    max_num, min_num = make_inequality_signs_num(n, current+str(i), visited, inequality_signs, max_num, min_num)
            else :
                # current가 비어 있을 때는 부등호 검사 없이 숫자 추가
                max_num, min_num = make_inequality_signs_num(n, current + str(i), visited, inequality_signs, max_num, min_num)
            visited.pop()  # 마지막에 추가된 숫자를 제거
    return max_num, min_num

n = int(input())
inequality_signs = input().split()
max_num, min_num = make_inequality_signs_num(n+1, '', [], inequality_signs, 0, float('inf'))
max_num = str(max_num)
min_num = str(min_num)
if len(max_num) == n:
    max_num = '0'+max_num
if len(min_num) == n:
    min_num = '0'+min_num
print(max_num)
print(min_num)
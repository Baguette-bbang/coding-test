from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    # 조합 만들고 조합에 각 지원자의 점수를 넣는다.
    # 점수의 리스트를 정렬한다.
    # 각 조건을 딕셔너리의 키로 넣은 다음 해당하는 밸류리스트를 얻고
    # 밸류 리스트에서는 이분 탐색을 진행한다.
    
    applicant_dict = {}
    for applicant in info: # 한 지원자의 정보
        applicant = applicant.split()
        for i in range(5): # 정보의 조합 0~4개 고르기까지 가능
            for com in combinations(applicant[:-1], i): # 조합 만들기
                key = ''.join(com) # 리스트를 문자열로 합치기
                if key in applicant_dict: # 해당 문자열이 있는가?
                    applicant_dict[key].append(int(applicant[-1])) # 해당 점수를 추가한다.
                else:
                    applicant_dict[key] = [int(applicant[-1])] 
    
    # 각 조건별 지원자 점수 정렬
    for key in applicant_dict.keys():
        applicant_dict[key].sort()

    for q in query:
        q_list = q.replace(" and ", " ").replace("-",'').split()
        q_score = int(q_list[-1])
        qstr = ''.join(q_list[:-1])
        if qstr in applicant_dict:
            idx = bisect_left(applicant_dict[qstr],q_score)
            answer.append(len(applicant_dict[qstr])-idx)
        else: 
            answer.append(0)

    return answer
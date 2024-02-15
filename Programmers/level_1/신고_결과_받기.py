from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    # 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송
    # 각 유저는 한 번에 한 명만 신고 가능
    # 서로 다른 유저를 계속해서 신고 가능
    # 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리
    # k번 이상 신고된 유저는 게시판 이용이 정지
    id_dict = defaultdict(int) # 신고 당한 횟수
    id_dict_singo = defaultdict(set) # 신고당한 유저를 신고한 유저를 저장
    
    # user2가 신고 당함
    # user1이 신고함.
    for user in set(report):
        user1, user2 = user.split()
        id_dict_singo[user2].add(user1)
        id_dict[user2] += 1 

    answer_dict = {}
    for id in id_list:
        answer_dict[id] = 0
        
    for id in id_list:
        if id_dict[id] >= k: # 신고당한 횟수
            for user in id_dict_singo[id]: # 해당 유저를 신고한 유저
                answer_dict[user] += 1
                
    answer = list(answer_dict.values())
    return answer
from collections import deque
def solution(record):
    answer = []
    # 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
    # 채팅방에서 닉네임을 변경
    # 유저 아이디가 같다면 마지막 닉네임이 진짜 닉네임이다.
    # 메세지를 출력해야 하는 것은 enter, leave이다.
    # 메세지 큐를 만들어놓고
    # 유저 아이디에 해당하는 닉네임을 매핑시킨다.
    message_queue = deque()
    name_dict = {}
    for r in record:
        r = r.split()
        flag, user_id, nickname = "", "", ""
        if len(r) >= 2:
            flag = r[0]
            user_id = r[1]
        if len(r) == 3:
            nickname = r[2]            
        if flag == "Enter":
            message_queue.append((user_id,"님이 들어왔습니다."))
        elif flag == "Leave":
            message_queue.append((user_id,"님이 나갔습니다."))
        if nickname != "":
            name_dict[user_id] = nickname
            
    while message_queue:
        message = message_queue.popleft()
        answer.append(name_dict[message[0]] + message[1])
        
    return answer
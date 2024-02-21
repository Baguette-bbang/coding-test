from collections import defaultdict
import re
def solution(files):
    answer = []
    # 50분 시작
    # 대소문자는 구별하지 않는다.
    # 일단 file명에 해당하는 것으로 묶는다.
    # file명은 따로 리스트로 관리 후 정렬시킨다.
    file_names = set()
    file_list = defaultdict(list)
    for file in files:
        temp = re.split(r'[.\s-]+', file)
        number= ''
        for c in temp:
            number = re.sub(r'\D','',c)
            if number != '':
                break
        idx = file.find(number)
        head = file[:idx]
        others = file[idx+len(number):]
        file_list[head.upper()].append((head, number, others, int(number)))
    
    file_list = sorted(file_list.items(), key = lambda x : x[0])
    for i in range(len(file_list)):
        sort_file = sorted(file_list[i][1], key = lambda x : x[-1])
        for j in range(len(sort_file)):
            answer.append(''.join(sort_file[j][:-1]))
    return answer
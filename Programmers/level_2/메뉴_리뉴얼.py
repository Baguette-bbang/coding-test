# 풀이 1
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    menu_combi = defaultdict(lambda : defaultdict(int))
    # 조합생성
    for order in orders:
        order = sorted(list(order))
        for i in range(2, len(order)+1):
            coms = list(combinations(order,i))
            for com in coms:
                menu_combi[len(com)][''.join(com)] += 1
    
    # course 길이에 해당하는 조합들만 뽑고 가장 긴 길이에 해당되는 음식들만 답에 입력
    for course_len in course:
        max_length = 0
        new_menu = sorted(menu_combi[course_len].items(), key = lambda x : x[1], reverse= True)
        if len(new_menu) > 0 and new_menu[0][1]>=2:
            max_length = new_menu[0][1]
            answer.append(new_menu[0][0])
            for i in range(1, len(new_menu)):
                if new_menu[i][1] == max_length:
                    answer.append(new_menu[i][0])
                else:
                    break
    return sorted(answer)


# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
# 풀이 2
from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    new_orders = [Counter() for _ in range(len(course))]
    for order in orders:
        for idx, size in enumerate(course):
            new_orders[idx].update(combinations(sorted(order),size))
    
    for order in new_orders: # 길이 
        if len(order) > 0 and max(order.values()) >= 2:
            for key, value in sorted(order.items(), key = lambda x : x[1], reverse = True):
                if value == max(order.values()):
                    answer.append(''.join(key))
                else:
                    break
                    
    return sorted(answer)
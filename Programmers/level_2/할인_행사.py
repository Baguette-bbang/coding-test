from collections import Counter
def solution(want, number, discount):
    answer = 0
    n = len(want)
    want_dict = sorted(dict(zip(want,number)).items(), key = lambda x : x[0])
    for i in range(len(discount)-9):
        new_discount = sorted(Counter(discount[i:i+10]).items(), key = lambda x : x[0])
        if len(new_discount) == n:
            cnt = 0
            for j in range(n):
                if want_dict[j][0] == new_discount[j][0] and want_dict[j][1] == new_discount[j][1]:
                    cnt += 1
                else: 
                    break
            if cnt == n:
                answer+=1
    return answer
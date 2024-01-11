# 볼에 해당 되는 숫자들을 알아야한다.
# 모든 경우의 수를 구하고
# 후보 숫자를 생성
n = int(input())
num = ['1','2','3','4','5','6','7','8','9']
# 모든 조합 생성하기
num_com = []
for n1 in num:
    for n2 in num:
        for n3 in num:
            if n1!=n2 and n2!=n3 and n1!=n3:
                num_com.append(n1+n2+n3)
def make_com(answer, temp_com, b, s):
    result = []
    list_answer = list(answer)
    for com in temp_com:
        temp_b, temp_s = 0,0 
        list_com = list(com)
        for i, c in enumerate(list_com):
            if c == list_answer[i]:
                temp_s += 1
            elif c in list_answer:
                temp_b += 1
        if temp_b == int(b) and temp_s == int(s):
            result.append(com)
    return result
temp_com = num_com.copy()
for i in range(n):
    answer, s, b = input().split()
    temp_com = make_com(answer, temp_com, b, s)

print(len(temp_com))
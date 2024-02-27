# 수가 보다 작은 자리의 수가 될 수 있음
n, k_num = map(int, input().split())
k_list = list(map(int, input().split()))
max_num = 0
max_len = len(str(n))
def make_largest(k_list, n, cur_num):
    global max_num
    
    if len(cur_num) > max_len: # 현재 숫자의 길이가 넘어가면 종료
        return
    
    if cur_num != '': # 빈 숫자가 아니면서 
        num = int(cur_num) 
        if num > n: # 비교 숫자보다 크다면 종료
            return
        else: # 비교 숫자보다 작거나 같다면
            max_num = max(max_num, num)
            
    for digit in k_list: # 업데이트
        make_largest(k_list, n, cur_num + str(digit))

make_largest(k_list, n, '')
print(max_num)
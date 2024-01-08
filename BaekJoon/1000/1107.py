# N과 최대한 비슷한 숫자로 이동
# +와 - 를 섞어서 이동
n = int(input())
error_button_num = int(input())
if error_button_num == 0:
    error_buttons = []
else: error_buttons = list(input().split())

# 남은 버튼에서 최대한 비슷한 버튼으로 이동
# n값하고 차이가 나지 않는 것으로 이동해야함.
# 최소한의 차이는 구했고 최소한의 차이인 경우의 current값을 반환하면 된다.
def switch_channel_by_button(error_buttons, n, min_num, current, close_num, length):
    if len(current) == length:
        return abs(n-int(current)), current
    for i in range(10):
        si = str(i)
        if si not in error_buttons:
            temp_min, temp_current = switch_channel_by_button(error_buttons, n, min_num, current+si, close_num, length)
            min_num = min(temp_min, min_num)
            if min_num == temp_min:
                close_num = temp_current
    return min_num, close_num
# 채널을 +,-로만 바꾸었을때 결과
min_pm = 0
if n>=100:
    min_pm = n-100
else:
    min_pm = 100-n
    
# 채널을 숫자 버튼으로 바꾸었을때 결과
if error_button_num == 10:
    print(min_pm)
else:
    min_num = float('inf')
    for i in range(1, len(str(n))+2):
        temp_min_num, temp_close_num = switch_channel_by_button(error_buttons, n, float('inf'), '', '', i)
        if min_num==temp_min_num:
            pass
        if min_num > temp_min_num:
            min_num = temp_min_num
            close_num = temp_close_num
    length = len(close_num)
    close_num = int(close_num)
    if close_num >=n:
        print(min(close_num-n+length,min_pm))
    else:
        print(min(n-close_num+length,min_pm))
# 에러처리1 : 10개 채널 다 망가진 경우 체크
# 에러처리2 : 자리수 다르게 하기(1~len(n)+2까지)자신의 자릿수를 초과하는 경우까지 생각해야함.
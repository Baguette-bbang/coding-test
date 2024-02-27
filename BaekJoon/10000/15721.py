a = int(input()) # 게임을 진행하는 사람
t = int(input()) # 구하고자하는 번째
n = int(input()) # 구하고하하는 구호

# 1. 라운드 구하기
fun_degi = 0 # 회차를 구하기 위한 뻔데기의 수
round = 0
while fun_degi < t: # 종료 조건은 fun_degi가 T개 이상으로 증가되는 회차
    round += 1
    fun_degi += 2 + round + 1
fun_degi -= 2 + round + 1
# print("round",round)
# print("fun_degi",fun_degi)

# 2. 해당 라운드를 시작하기 전까지 진행됐던 사람 번째
turn = (fun_degi*2-1)%a # 진행회차 전까지의 사람
# 의문 진행회차 전까지의 사람이 없다면? 즉, 1회차에서 끝난다면?
# print("turn",turn)
# 3. 해당 라운드 시작
fun_degi_list = [0,1,0,1] # 뻔, 데기, 뻔, 데기로 시작
fun_degi_list += [0 for _ in range(round+1)]
fun_degi_list += [1 for _ in range(round+1)]
#print(fun_degi_list)
fun = fun_degi
degi = fun_degi
for fun_or_degi in fun_degi_list:
    if fun_or_degi == 0:
        fun += 1
    else:
        degi += 1
    turn = (turn + 1) % a
    if n == 0 and fun == t:
        print(turn)
        break
    if n == 1 and degi == t:
        print(turn)
        break
    
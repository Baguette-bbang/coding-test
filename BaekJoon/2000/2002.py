# 추월 : 자신의 앞차량 중 하나라도 앞서 갔다는 의미
# 시간 상 For 문 2번 가능할 듯

n = int(input())
in_cars = dict()
out_cars = dict()
in_cars_list = [] # 들어온 순서 저장용

for i in range(n):
    car = input()
    in_cars[car] = i
    in_cars_list.append(car)
    
for i in range(n):
    car = input()
    out_cars[car] = i
#############################    

# 제일 앞서 가던 차량은 추월 여부를 알 수 없음
# print(in_cars, out_cars)

answer = 0
for i in range(1, n):
    car = in_cars_list[i] # 현재 추월여부 확인 차량
    front_cars = in_cars_list[:i] # 앞서 가던 차량들
    for fcar in front_cars:
        # 하나라도 앞서져 있다면
        if out_cars[fcar] > out_cars[car]:
            answer +=1
            break
print(answer)
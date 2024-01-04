### 풀이 1 ###
def find_combination(current, num):
    if current == num:
        return 1
    if current > num:
        return 0
    cnt = 0
    for i in range(1,4):
        cnt += find_combination(current+i, num)
    return cnt

sum_combinaiton = [] 
for i in range(1, 11):
    sum_combinaiton.append(find_combination(0, i))

t = int(input())
for _ in range(t):
    i = int(input())
    print(sum_combinaiton[i-1])
    
### 풀이 2 ###
sum_combinaiton = [1,2,4] 
for i in range(3, 11):
    n_sum = sum_combinaiton[i-1] + sum_combinaiton[i-2] + sum_combinaiton[i-3]
    sum_combinaiton.append(n_sum)

t = int(input())
for _ in range(t):
    i = int(input())
    print(sum_combinaiton[i-1])

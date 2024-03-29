s = input()
one = s.split("1")
zero = s.split("0")
one_cnt = 0
zero_cnt = 0
for i in range(len(one)) : 
    if one[i] != '':
        one_cnt += 1

for i in range(len(zero)) : 
    if zero[i] != '':
        zero_cnt += 1

print(min(one_cnt, zero_cnt))
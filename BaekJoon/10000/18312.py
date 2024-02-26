answer = 0
n, num = map(int, input().split())
num = str(num)
for i in range(n+1):
    if i< 10:
        i = '0' + str(i)
    else:
        i = str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        else:
            j = str(j)
        for k in range(60):
            if k < 10:
                k = '0' + str(k)
            else:
                k = str(k)
            if num in i+j+k:
                answer += 1
print(answer)
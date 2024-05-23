problems = dict()
for i in range(1,9):
    problems[i] = int(input())
    
problems = sorted(problems.items(), key = lambda x : -x[1])[:5]

sum = 0
for p in problems:
    sum += p[1]
print(sum)

answer = []
for i in range(5):
    answer.append(problems[i][0])
answer.sort()
print(*answer)
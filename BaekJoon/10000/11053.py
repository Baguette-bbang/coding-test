n = int(input()) # 입력 숫자의 수
sequence = list(map(int, input().split())) # 입력 수열
d = [1] * n # d 초기화
# i의 뒤에 있는 인덱스들에서 가장 최대값을 찾는데 그 수가 나보다 작아야함.
for i in range(1,n): # 길이가 2인 것들부터 탐색 
    max_value = 0
    for j in range(i): # 선정된 인덱스에서 뒤에까지 최대 길이
        if sequence[i] > sequence[j]:
            max_value = max(max_value, d[j])
    d[i] += max_value
print(max(d))

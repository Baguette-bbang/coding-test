# 백준 2037번 문자메시지 - 브론즈1
num_dict = {
    2 : ['A', 'B', 'C'],
    3 : ['D', 'E', 'F'],
    4 : ['G', 'H', 'I'],
    5 : ['J', 'K', 'L'],
    6 : ['M', 'N', 'O'],
    7 : ['P', 'Q', 'R', 'S'],
    8 : ['T', 'U', 'V'],
    9 : ['W', 'X', 'Y', 'Z']
}

p, w = map(int, input().split())
# 같은 번호에 있는 알파벳이라면 기다려야 하는 초가 있다.
alphas = input()

# 알파벳 - 숫자로 매핑시키기
char_to_num = {}
for key, value in num_dict.items():
    for i, char in enumerate(value):
        # 키, 번째로 이루어짐
        char_to_num[char] = (key, i + 1)

# print(char_to_num)

# 기다려야 하는 시간
last_key = None # 알파벳 제외 아무 문자
time = 0
for char in alphas:
    # 공백 처리
    if char == ' ': 
        time += p
        last_key = None
    else:
        key, position = char_to_num[char]
        time += position * p
        # 같은 키가 연속으로 입력되는지
        if key == last_key:
            time += w
        last_key = key
print(time)
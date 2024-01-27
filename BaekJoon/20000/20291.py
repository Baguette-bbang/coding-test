# 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘
# 보기 편하게 확장자들을 사전 순으로 정렬해 줘

dict = {}
# 파일이 뭔지는 무시해도 됨.
# 그저 확장자만이 중요함.
# 즉, .이후의 단어에 대해 
n = int(input())
for i in range(n):
    file = input()
    idx = file.find('.')
    extension= file[idx+1:]
    if extension not in dict:
        dict[extension] = 1 
    else:
        dict[extension] += 1
extensions = sorted(dict)
for extension in extensions:
    print(extension, dict[extension])
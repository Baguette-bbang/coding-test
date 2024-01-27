n = int(input()) # 파일의 수 
extension_count = {} # 각 파일에서 확장자가 뭔지 구하고 각 확장자의 개수를 구해야함.
for i in range(n):
    extension = input().split(".")[-1] # 파일은 파일명과 확장자로 구성되어 있으며 구분하는 것은 "."에 의해서임.
    extension_count[extension] = extension_count.get(extension,0) + 1 # extension에 해당하는 값이 있다면 해당 값을 가져온 후 +1 없다면 0을 반환하여 +1
for extension in sorted(extension_count):
    print(extension, extension_count[extension])
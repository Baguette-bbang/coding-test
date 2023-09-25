s = input()
for i in range(len(s)):
    print(s[i], end="")
    if i%2==1:
        print(" ", end="")
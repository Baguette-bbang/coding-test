n = int(input())
for _ in range(n):
    b1, b2 = input().split()
    print(format(int('0b' + b1, 2) + int('0b' + b2, 2),'b'))
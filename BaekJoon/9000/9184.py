import sys 
input = sys.stdin.readline
w_dict = {(0,0,0):1}

def w(a,b,c):
    global w_dict
    if (a,b,c) in w_dict:
        return w_dict[(a,b,c)]
    elif a<=0 or b<=0 or c<=0:
        w_dict[(a,b,c)] = 1
    elif a>20 or b>20 or c>20:
        w_dict[(a,b,c)] = w(20,20,20)
    elif a<b and b<c:
        w_dict[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        w_dict[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return w_dict[(a,b,c)]

while(1):
    a, b, c = map(int, input().split())
    answer = 0
    if a == -1 and b == -1  and c == -1 :
        break
    else:
        answer = w(a,b,c)
    print(f"w({a}, {b}, {c}) = {answer}")
    
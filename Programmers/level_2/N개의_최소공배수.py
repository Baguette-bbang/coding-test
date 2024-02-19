from math import gcd
def solution(arr):
    def lcm(x, y):
        return x*y // gcd(x,y)
    while len(arr) > 1:
        new = lcm(arr.pop(), arr.pop())
        arr.append(new)
        if len(arr) == 1:
            return arr[0]
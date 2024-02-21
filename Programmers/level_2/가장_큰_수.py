from functools import cmp_to_key
def solution(numbers):
    def compare(x, y):
        if x + y < y + x:
            return 1
        return -1
    numbers = sorted(list(map(str, numbers)), key=cmp_to_key(compare))
    return str(int(''.join(numbers)))
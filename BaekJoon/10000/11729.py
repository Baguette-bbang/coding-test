n = int(input())
print(2**n-1)
def move_hanoi(start_peg, end_peg):
    print(start_peg, end_peg)
def hanoi(n, start_peg, end_peg, other_peg):
    # 종료 조건
    if n==1:
        move_hanoi(start_peg, end_peg)
    else:
        hanoi(n-1, start_peg, other_peg, end_peg)
        move_hanoi(start_peg, end_peg)
        hanoi(n-1, other_peg, end_peg, start_peg)
hanoi(n, 1, 3, 2)
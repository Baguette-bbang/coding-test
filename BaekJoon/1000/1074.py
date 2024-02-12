n, r, c = map(int, input().split())
n = 2**n

def visit_array(x, y, size, cnt):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if i == r and j == c:
                print(cnt)
                exit(0)
            cnt += 1

def divide_array(x, y, size, cnt):
    if size == 1:
        visit_array(x, y, size, cnt)
        return
    new_size = size // 2
    for i in range(2):
        for j in range(2):
            print(x + i * new_size, x + (i + 1) * new_size)
            print(y + j * new_size, y + (j + 1) * new_size)
            if x + i * new_size <= r < x + (i + 1) * new_size and y + j * new_size <= c < y + (j + 1) * new_size:
                divide_array(x + i * new_size, y + j * new_size, new_size, cnt)
            cnt += new_size ** 2

divide_array(0, 0, n, 0)

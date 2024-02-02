from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
op_counts = list(map(int, input().split()))  # 각 연산자의 개수

operators = "+" * op_counts[0] + "-" * op_counts[1] + "*" * op_counts[2] + "/" * op_counts[3]

op_set_permutations = set(permutations(operators, n-1))

def cal(operators_set, numbers):
    calculated_num = numbers[0]
    for idx, operator in enumerate(operators_set):
        if operator == '+':
            calculated_num += numbers[idx+1]
        elif operator == '-':
            calculated_num -= numbers[idx+1]
        elif operator == '*':
            calculated_num *= numbers[idx+1]
        else:
            if calculated_num < 0:
                calculated_num = -(-calculated_num // numbers[idx+1])
            else:
                calculated_num //= numbers[idx+1]
    return calculated_num
min_value, max_value = float('inf'), float('-inf')
for operators_set in op_set_permutations:
    calculated_num = cal(operators_set, numbers)
    min_value = min(min_value, calculated_num)
    max_value = max(max_value, calculated_num)
print(max_value)
print(min_value)
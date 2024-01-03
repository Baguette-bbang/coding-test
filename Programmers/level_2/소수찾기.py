def make_combination(numbers, used, current, combination):
    if len(current) > 0:
        combination.add(current)

    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            make_combination(numbers, used, current + numbers[i], combination)
            used[i] = False
            
def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    combination = set()
    used = [False] * len(numbers)

    make_combination(numbers, used, "", combination)

    combination = set(map(int, combination))
    
    for num in combination:
        if num > 1 and all(num % j != 0 for j in range(2, int(num ** 0.5) + 1)):
            answer += 1

    return answer
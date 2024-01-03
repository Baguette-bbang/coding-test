def find_combinations(current_combi, alphabet, length, combinations):
    if length == 0:
        combinations.add(current_combi)
        return 
    for alpha in alphabet:
        find_combinations(current_combi+alpha, alphabet, length-1, combinations)
    return combinations
def solution(word):
    combinations = set()
    alphabet = ['A', 'E', 'I', 'O', 'U']
    temp1=set()
    for i in range(1, 6): # 모든 알파벳 길이의 조합
        temp = set()
        temp = find_combinations('', alphabet, i, temp)
        for t in temp:
            combinations.add(t)
    combinations = sorted(list(combinations))
    return combinations.index(word)+1
from collections import defaultdict
def solution(n, words):
    answer = [0,0]
    word_list = defaultdict(int)
    word_list[words[0]] += 1
    for idx, word in enumerate(words[1:]):
        word_list[word] += 1
        if word_list[word] >= 2 or words[idx][-1] != words[idx+1][0]:
            print(words[idx][-1], words[idx+1][0])
            return [(idx+1)%n+1, (idx+1)//n+1 ]    
    return answer
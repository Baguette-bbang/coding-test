from collections import Counter
def solution(nums):
    answer = 0
    # 카운터로 각 포켓몬의 개수를 센다
    # 각 종류별로 순회를 하면서 1개씩 뺀다
    # 해당 종류가 0개가 되면 del 한다.
    # 이것이 len(nums) // 2 개수가 될 때 까지 반복한다.
    # 답은 set()의 길이로 처리
    counter_monster = Counter(nums)
    num = 0
    answer = set()
    while num < len(nums)//2:
        monster = list(counter_monster.keys())
        for i in range(len(monster)):
            counter_monster[monster[i]] -= 1
            answer.add(monster[i])
            num += 1
            if num == len(nums)//2:
                break
            if counter_monster[monster[i]] == 0:
                del counter_monster[monster[i]]
            
    return len(answer)
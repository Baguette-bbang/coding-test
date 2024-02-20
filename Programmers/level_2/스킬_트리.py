import re
def solution(skill, skill_trees):
    answer = 0
    result = map(str,[i for i in range(1, len(skill)+1)])
    result = ''.join(result)
    my_skills = list(skill)
    for skill_tree in skill_trees:
        for idx, my_skill in enumerate(my_skills):
            skill_tree = skill_tree.replace(my_skill, str(idx+1))
        filtered_skill_tree = re.sub("[a-zA-Z]", "", skill_tree)
        
        for i in range(len(filtered_skill_tree)):
            if filtered_skill_tree[i] != result[i]:
                break
        else:
            answer += 1    

    return answer
import re

def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in skill_trees:
        check = ""
        k = 0
        for j in i:
            if j in skill:
                if skill[k] == j:
                    k += 1
                    pass
                else:
                    answer -= 1
                    break
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

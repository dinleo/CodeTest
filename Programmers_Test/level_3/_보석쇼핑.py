# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
from collections import defaultdict


def solution(gems):
    g = list(set(gems))
    g_dict = defaultdict(int)
    for i in range(len(g)):
        g_dict[g[i]] = i
    answer = [0,100000]
    g_num = [100000 for _ in range(len(g))]
    best = 100000
    for i in range(len(gems)):
        g_num[g_dict[gems[i]]] = i
        i_max, i_min = max(g_num), min(g_num)
        if i_max - i_min < best:
            best = i_max - i_min
            answer[0], answer[1] = i_min+1, i_max+1


    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
from collections import defaultdict


def solution(gems):
    g_dict = defaultdict(list)

    for i in range(len(gems)):
        g_dict[gems[i]].append(i)
        
    answer = []

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
from collections import defaultdict


def solution(gems):
    i_max, i_min = 100000, 0

    # key = 보석이름, value = 인덱스 인 dict 를 생성
    g_set = set(gems)
    g_dict = defaultdict(int)
    for g in g_set:
        g_dict[g] = -1

    # 모든 보석의 인덱스가 담길 때까지 gems 를 스캔후, 가장 낮은 인덱스와 보석이름을 저장
    for i in range(len(gems)):
        g_dict[gems[i]] = i
        if -1 not in g_dict.values():
            i_max = i
            break

    i_min = min(g_dict.values())
    min_gem = gems[i_min]

    # 모든 보석이 담긴 구역중 최소구역의 길이
    best = i_max - i_min
    answer = [i_min+1,i_max+1]

    # i_max 부터 스캔을 시작해 min_gem 이 등장하면 i_min 과 best 를 갱신한다.
    for i in range(i_max+1, len(gems)):
        gem = gems[i]
        g_dict[gem] = i
        if gem == min_gem:
            i_max = i
            i_min = min(g_dict.values())
            min_gem = gems[i_min]
            if i_max-i_min < best:
                best = i_max-i_min
                answer = [i_min + 1, i_max + 1]

    return answer




print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY", "EMERALD", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
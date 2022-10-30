# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
from collections import defaultdict


def solution(clothes):
    dic = defaultdict(list)
    for c in clothes:
        dic[c[1]].append(c[0])
    answer = 1
    print(dic)
    for d in dic:
        answer *= (len(dic[d]) + 1)
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
